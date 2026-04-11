# LLM Wiki — Karpathy Metodu

**Kişisel bilgi tabanı** — LLM tarafından yönetilen, sürekli güncellenen wiki sistemi.

---

## 📁 Yapı

```
/root/obsidian/vault/
├── raw/              # Kaynak dokümanlar (IMMUTABLE - sadece oku)
│   ├── articles/     # Web makaleleri
│   ├── papers/       # PDF'ler, araştırma notları
│   ├── books/        # Kitap notları
│   ├── transcripts/  # Podcast/video transcript
│   └── assets/       # Resimler
│
├── wiki/             # LLM'in yazdığı sayfalar (LLM-OWNED - sürekli güncelle)
│   ├── summaries/    # Kaynak özetleri
│   ├── entities/     # Kişiler, şirketler
│   ├── concepts/     # Kavramlar, teoriler
│   ├── comparisons/  # Karşılaştırmalar
│   └── synthesis/    # Büyük resim
│
├── index.md          # Wiki katalogu (LLM her ingest'te günceller)
├── log.md            # İşlem geçmişi (append-only)
│
├── query.py          # CLI sorgu aracı
└── lint.py           # Sağlık kontrolü
```

---

## 🚀 Kullanım

### 1. INGEST (Kaynak Ekleme)

Yeni bir makale/doküman eklemek için:

1. Kaynağı `raw/articles/` altına koy (Obsidian Web Clipper ile veya manuel)
2. Claude'a söyle: **"Bu kaynağı ingest et"**

Claude:
- Kaynağı okur ve analiz eder
- Key takeaway'leri seninle tartışır
- `wiki/summaries/` altına özet sayfası yazar
- İlgili entity/concept sayfalarını oluşturur/günceller
- `index.md` ve `log.md`'yi günceller

**Örnek:**
```
raw/articles/attention-mechanism.md ekledim
→ Claude: "Bu makaleyi ingest et"
→ 6 wiki sayfası oluşturuldu (1 özet, 2 entity, 3 concept)
```

---

### 2. QUERY (Sorgulama)

Wiki'den bilgi çekmek için:

**Claude ile (manuel):**
```
"Transformer mimarisi nedir?"
```

Claude:
- `index.md`'yi okur
- İlgili sayfaları bulur ve okur
- Sentezleyip kaynaklarla cevap verir

**CLI ile (otomatik):**
```bash
python query.py "transformer"
python query.py "attention mechanism" --file-back  # Cevabı kaydet
```

---

### 3. LINT (Sağlık Kontrolü)

Wiki'yi periyodik olarak kontrol et:

```bash
python lint.py
```

Kontroller:
- ✅ Bitik linkler (broken wikilinks)
- ✅ Yetim sayfalar (orphan pages)
- ✅ Eski sayfalar (30+ gün güncellenmeyen)
- ✅ İşlenmemiş kaynaklar (raw/ dosyaları)

---

## 📝 Kurallar

### ✅ YAPILACAKLAR
- `raw/` dosyalarını **sadece oku**, asla değiştirme
- Wiki sayfalarında `[[wikilink]]` formatı kullan
- Her sayfa frontmatter içermeli:
  ```yaml
  ---
  title: Başlık
  date: YYYY-MM-DD
  tags: [tag1, tag2]
  sources: [kaynak1]
  ---
  ```
- `index.md` ve `log.md`'yi her ingest'te güncelle

### ❌ YAPILMAYACAKLAR
- `raw/` dosyalarını silme/değiştirme
- Wiki dışı yerlere wiki sayfası yazma
- `index.md` veya `log.md`'yi silme

---

## 🛠️ Obsidian Entegrasyonu

### Gerekli Eklentiler
1. **Web Clipper** (browser extension) — Web makalelerini markdown'a çevir
2. **Dataview** (Obsidian plugin) — Frontmatter sorgulama
3. **Graph View** — Bağlantıları görselleştir

### Ayarlar
- Settings → Files and links → Attachment folder: `raw/assets/`
- Hotkey: Ctrl+Shift+D → "Download attachments for current file"

---

## 📊 Durum

**Mevcut Wiki:**
- Total Pages: 6
- Total Sources: 1
- Last Ingest: 2026-04-11

---

## 🔗 Kaynaklar

- [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- CLAUDE.md — Talimat dosyası

---

**Not:** Bu sistem test fazında. Production kullanım için automation scriptlerini geliştir (compile.py, cron jobs, vb.)
