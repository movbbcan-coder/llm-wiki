---
ureten: hafiza-yayinla
tip: ders
no: 57
etiketler: [ders, rulebook]
---

# Ders 57 — Prepaid kredi izlenen kullanımdan HIZLI eriyorsa, aynı faturaya bağlı BAŞKA servisleri ara — tek izlenen kalem suçlu sanılır.

**Prepaid kredi izlenen kullanımdan HIZLI eriyorsa, aynı faturaya bağlı BAŞKA servisleri ara — tek izlenen kalem suçlu sanılır.** Gemini prepay kredisi "bitti/-43₺" görünüyordu; bakiye nöbetçisi yalnız OCR (dekont/beyin) çağrılarını sayıyordu. Google Cloud taraması: aynı faturalama hesabında (016DFA) **2 Cloud Run relay'i min-instances=1 ile 7/24 açıktı** (donuk VPN'in front'u, kimse kullanmıyor) → her biri ~$10-15/ay krediyi sessizce yiyordu. Yani "kredi bitti" kısmen OCR değil, izlenmeyen Cloud Run'dı. Fix: min-instances=0 (bostayken $0, config yedekli, reversible). İKİNCİ: OCR modeli `gemini-flash-latest` (alias) fiyat tablosunda yoktu → en pahalıdan sayılıyordu (over-count ~4-5×, "en pahalı bilinen fiyat" muhafazakârlığı canlı doğrulandı) + gp1 429 veriyordu. `gemini-2.5-flash-lite`'a sabitlendi (0.10/0.40, ~15× ucuz), 3 gerçek fişte doğruluk teyit edildi. ÜÇÜNCÜ: fiş dedup hash'i kaydet()'te (OCR'dan SONRA) kontrol ediliyordu → aynı foto tekrar OCR'a para harcıyordu; parse()'a OCR-öncesi cache eklendi (hata cache'lenmez — geçici 503 zehirlemesin).

---
*Kaynak: Gemini kredi + Cloud Run gizli musluk 2026-08-11 → vision_gateway/.env VG_FLASH_MODEL + bakiye_nobetci FIYAT + gider_foto OCR cache + test_gider_foto_dedup.py*
