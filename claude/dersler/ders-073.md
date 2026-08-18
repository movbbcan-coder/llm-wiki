---
ureten: hafiza-yayinla
tip: ders
no: 73
etiketler: [ders, rulebook]
---

# Ders 73 — Aynı olayı iki ekran listeliyorsa gün hesabı da kopyalanır ve bir gün ayrışır.

**Aynı olayı iki ekran listeliyorsa gün hesabı da kopyalanır ve bir gün ayrışır.** Akış ekranı Netflix için *"6 Eyl · 28 gün"*, Bütçe ekranındaki "Yaklaşan ödemeler" AYNI kayıt için *"27 gün sonra"* diyordu: Akış `LocalDate` farkı (takvim günü) sayıyor, `YukumlulukTespiti.neZaman` millis farkını `roundToLong` ile yuvarlıyor (21:44'te 27,1 gün → 27). İkisi de "doğru" hesap, ama kullanıcı iki ekranda iki sayı görüyor. Kopya listeyi silmek tek çözümdü: yaklaşan ödemelerin LİSTESİ tek ekranda (Akış) kaldı, Bütçe ekranı yalnız bütçe bağlamında anlamlı olanı söylüyor (aylık düzenli yük toplamı + "akışta gör ›"). **Kural: aynı olguyu iki ekran gösteriyorsa yalnız SAYIYI değil, sayıyı üreten hesabı da ortaklaştır; ortaklaştıramıyorsan ikinci listeyi kaldırıp birinciye link ver.** Not: hatayı 190 birim testi + 26 Paparazzi render'ı DEĞİL, cihazda iki ekranı arka arkaya açmak yakaladı (#63'ün tekrarı — render testi bileşeni yalıtılmış çizer, iki ekranı KIYASLAMAZ).

---
*Kaynak: Denk Akış/Bütçe gün ayrışması 2026-08-09 → ButceEkrani düzenli yük özeti + Akis SSOT*
