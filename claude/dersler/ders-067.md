---
ureten: hafiza-yayinla
tip: ders
no: 67
etiketler: [ders, rulebook]
---

# Ders 67 — Tanıtım/mağaza görseline GERÇEK kullanıcı verisi girer — demo defter kurmadan ekran görüntüsü alma.

**Tanıtım/mağaza görseline GERÇEK kullanıcı verisi girer — demo defter kurmadan ekran görüntüsü alma.** Denk'in ilk Play ekran görüntüleri kullanıcının gerçek harcamalarını taşıyordu: Anthropic 1.148,88 ₺, Google 1.043,75 ₺, gerçek banka bakiyeleri. Yayınlansaydı kişinin aylık harcama dökümü herkese açık olacaktı. Fark edilme sebebi görseli gözle incelemekti; üretim boru hattı hiçbir uyarı vermiyordu. Fix: üreteç script YALNIZ `ss_demo/` klasöründen besleniyor, o klasör `pm clear` + sahte bildirim enjeksiyonuyla kurulan KURGU bir defterden çekiliyor. İKİNCİ DERS — spec'i ölçmeden üretme: telefonun ham ekran görüntüsü 1080×2340, oran 2,17; Google **"uzun kenar kısa kenarın 2 katından fazla olamaz"** diyor → olduğu gibi yüklense REDDEDİLİRDİ. Üreteç artık her dosyayı spec'e karşı ölçüp raporluyor. ÜÇÜNCÜ: görseli script üret — elle yapılan görsel ekran değişince bayatlar ve mağazada artık var olmayan bir ekran gösterir.

---
*Kaynak: Denk mağaza görselleri 2026-08-09 → magaza/uret.py + ss_demo/ + METINLER.md*
