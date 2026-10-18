#!/usr/bin/env python3
"""
query.py - Wiki sorgulama CLI aracı

Kullanım:
  python query.py "soru"
  python query.py "soru" --file-back  # Cevabı wiki/synthesis/ altına kaydet
"""

import sys
import os
from datetime import datetime

VAULT_PATH = "/root/obsidian/vault"
INDEX_PATH = f"{VAULT_PATH}/index.md"
WIKI_PATH = f"{VAULT_PATH}/wiki"


def search_index(query):
    """index.md'de arama yap"""
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Basit keyword search
    lines = content.split('\n')
    results = []
    
    for line in lines:
        if '[[' in line and any(keyword.lower() in line.lower() for keyword in query.split()):
            results.append(line.strip())
    
    return results


def read_page(page_name):
    """Wiki sayfasını oku"""
    # Olası lokasyonlar
    locations = [
        f"{WIKI_PATH}/summaries/{page_name}.md",
        f"{WIKI_PATH}/entities/{page_name}.md",
        f"{WIKI_PATH}/concepts/{page_name}.md",
        f"{WIKI_PATH}/synthesis/{page_name}.md",
    ]
    
    for loc in locations:
        if os.path.exists(loc):
            with open(loc, 'r', encoding='utf-8') as f:
                return f.read()
    
    return None


def main():
    if len(sys.argv) < 2:
        print("Kullanım: python query.py 'soru' [--file-back]")
        sys.exit(1)
    
    query = sys.argv[1]
    save_to_file = '--file-back' in sys.argv
    
    print(f"🔍 Sorgu: {query}\n")
    
    # 1. Index'te ara
    print("📚 Index'te arıyorum...")
    results = search_index(query)
    
    if not results:
        print("❌ İlgili sayfa bulunamadı.")
        sys.exit(0)
    
    print(f"✅ {len(results)} sayfa bulundu:\n")
    for r in results:
        print(f"  - {r}")
    
    print("\n" + "="*60)
    print("📖 Cevap:\n")
    print(f"Sorgu: '{query}' için wiki'de bulunan bilgiler:\n")
    
    # Bu noktada normalde LLM sayfaları okur ve sentezler
    # Şimdilik sadece bulduğumuz sayfaları gösterelim
    print("İlgili sayfalar:")
    for r in results:
        print(f"  - {r}")
    
    print("\n💡 Not: Tam sentez için LLM gerekli (Claude/GPT)")
    print("="*60)
    
    if save_to_file:
        # Cevabı synthesis/ altına kaydet
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = f"{WIKI_PATH}/synthesis/{timestamp}-query-{query[:20].replace(' ', '-')}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Query: {query}\n\n")
            f.write(f"**Date:** {timestamp}\n\n")
            f.write("## Results\n\n")
            for r in results:
                f.write(f"- {r}\n")
        
        print(f"\n💾 Cevap kaydedildi: {filename}")


if __name__ == "__main__":
    main()
