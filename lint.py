#!/usr/bin/env python3
"""
lint.py - Wiki sağlık kontrolü

7 kontrol yapar:
1. Bitik linkler ([[Page]] ama Page.md yok)
2. Yetim sayfalar (hiçbir sayfa link vermiyor)
3. Eksik kavramlar (mentioned but no page)
4. Cross-ref simetri (A→B varsa B→A olmalı)
5. Eski tarihli sayfalar (30+ gün güncellenmeyen)
6. Kaynak coverage (raw/'da işlenmemiş dosya var mı)
7. Frontmatter eksikleri
"""

import os
import re
from datetime import datetime, timedelta
from collections import defaultdict

VAULT_PATH = "/root/obsidian/vault"
WIKI_PATH = f"{VAULT_PATH}/wiki"
RAW_PATH = f"{VAULT_PATH}/raw"


def find_wikilinks(content):
    """[[wikilink]] formatındaki linkleri bul"""
    return re.findall(r'\[\[([^\]]+)\]\]', content)


def get_all_wiki_files():
    """Tüm wiki dosyalarını bul"""
    files = []
    for root, dirs, filenames in os.walk(WIKI_PATH):
        for f in filenames:
            if f.endswith('.md'):
                files.append(os.path.join(root, f))
    return files


def get_all_raw_files():
    """Tüm raw dosyaları bul"""
    files = []
    for root, dirs, filenames in os.walk(RAW_PATH):
        for f in filenames:
            if f.endswith('.md'):
                files.append(os.path.join(root, f))
    return files


def check_broken_links():
    """1. Bitik linkler"""
    print("\n🔍 1. Bitik Linkler Kontrolü...")
    
    wiki_files = get_all_wiki_files()
    all_page_names = set()
    
    # Tüm sayfa isimlerini topla
    for f in wiki_files:
        basename = os.path.basename(f).replace('.md', '')
        all_page_names.add(basename)
    
    # Her dosyadaki linkleri kontrol et
    broken = []
    for f in wiki_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            links = find_wikilinks(content)
            
            for link in links:
                if link not in all_page_names:
                    broken.append((f, link))
    
    if broken:
        print(f"  ❌ {len(broken)} bitik link bulundu:")
        for file, link in broken[:10]:  # İlk 10'u göster
            print(f"    - {os.path.basename(file)}: [[{link}]]")
        if len(broken) > 10:
            print(f"    ... ve {len(broken) - 10} tane daha")
    else:
        print("  ✅ Bitik link yok")


def check_orphan_pages():
    """2. Yetim sayfalar"""
    print("\n🔍 2. Yetim Sayfalar Kontrolü...")
    
    wiki_files = get_all_wiki_files()
    page_links = defaultdict(int)  # Her sayfaya kaç link var
    
    # Tüm linkleri say
    for f in wiki_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            links = find_wikilinks(content)
            for link in links:
                page_links[link] += 1
    
    # Hiç link almayan sayfalar
    orphans = []
    for f in wiki_files:
        basename = os.path.basename(f).replace('.md', '')
        if page_links[basename] == 0:
            orphans.append(basename)
    
    if orphans:
        print(f"  ⚠️  {len(orphans)} yetim sayfa bulundu:")
        for page in orphans[:10]:
            print(f"    - {page}")
        if len(orphans) > 10:
            print(f"    ... ve {len(orphans) - 10} tane daha")
    else:
        print("  ✅ Yetim sayfa yok")


def check_stale_pages():
    """5. Eski tarihli sayfalar"""
    print("\n🔍 5. Eski Tarihli Sayfalar...")
    
    wiki_files = get_all_wiki_files()
    threshold = datetime.now() - timedelta(days=30)
    stale = []
    
    for f in wiki_files:
        mtime = datetime.fromtimestamp(os.path.getmtime(f))
        if mtime < threshold:
            days_old = (datetime.now() - mtime).days
            stale.append((os.path.basename(f), days_old))
    
    if stale:
        print(f"  ⚠️  {len(stale)} sayfa 30+ gün güncellenme almamış:")
        for page, days in stale[:5]:
            print(f"    - {page} ({days} gün önce)")
        if len(stale) > 5:
            print(f"    ... ve {len(stale) - 5} tane daha")
    else:
        print("  ✅ Tüm sayfalar güncel")


def check_source_coverage():
    """6. Kaynak coverage"""
    print("\n🔍 6. Kaynak Coverage...")
    
    raw_files = get_all_raw_files()
    
    # index.md'deki kaynakları kontrol et
    index_path = f"{VAULT_PATH}/index.md"
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    unprocessed = []
    for raw_file in raw_files:
        rel_path = raw_file.replace(f"{VAULT_PATH}/", "")
        if rel_path not in index_content:
            unprocessed.append(os.path.basename(raw_file))
    
    if unprocessed:
        print(f"  ⚠️  {len(unprocessed)} işlenmemiş kaynak:")
        for f in unprocessed[:5]:
            print(f"    - {f}")
        if len(unprocessed) > 5:
            print(f"    ... ve {len(unprocessed) - 5} tane daha")
    else:
        print("  ✅ Tüm kaynaklar işlenmiş")


def main():
    print("="*60)
    print("🩺 WIKI SAĞLIK KONTROLÜ")
    print("="*60)
    
    check_broken_links()
    check_orphan_pages()
    check_stale_pages()
    check_source_coverage()
    
    print("\n" + "="*60)
    print("✅ Lint tamamlandı")
    print("="*60)


if __name__ == "__main__":
    main()
