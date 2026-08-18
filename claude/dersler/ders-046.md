---
ureten: hafiza-yayinla
tip: ders
no: 46
etiketler: [ders, rulebook]
---

# Ders 46 — Uzun/arka-plan iş, diske checkpoint yazmadan canlı sürece güvenirse session ölünce iz bırakmadan uçar.

**Uzun/arka-plan iş, diske checkpoint yazmadan canlı sürece güvenirse session ölünce iz bırakmadan uçar.** 33-ajanlı deep-research workflow'u canlı bellekte çalıştı, `writeFile` yoktu; hesap geçişinde (claude1→claude2) session ölünce tüm araştırma gitti (Fetch 19/26'da kesildi, sentez hiç başlamadı, `/workflows` taze session'da onu göremez). **Kural: uzun sürecek VEYA arka planda dönecek her iş, başlamadan `/root/claude/is_defteri/<tarih-slug>/` açar; PLAN.md + DURUM.json (checkpoint) + bulgular/ (adım adım) + RAPOR.md yazar. Arka-plan sürücü `nohup` ile başlar (session'dan bağımsız yaşar). Session ölürse DURUM.json'daki `sonraki`den devam — biten adımı TEKRARLAMA.** İki yan-ders: (a) rate-limitli API'de (jc free = 5/dk) istekler arası throttle+retry+min-boyut kapısı şart, yoksa 429 çıktısı 1-byte çöp dosya olur ve "dolu" sanılır; (b) jc çalışma dizinindeki dosyaları okur — konu-dışı dosya varsa (PLAN.md/DURUM.json) konuyu bırakıp onları konuşur, araştırmayı temiz/boş dizinden koş.

---
*Kaynak: deep-research kaybı 2026-07-25 → /root/claude/is_defteri/ + README.md kuralı*
