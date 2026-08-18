---
ureten: hafiza-yayinla
tip: ders
no: 66
etiketler: [ders, rulebook]
---

# Ders 66 — Bir payı bir paydaya bölmeden önce "bu ikisi AYNI zaman penceresinden mi?" diye sor — modül doğru olsa bile girdiler ayrışırsa sonuç yalan olur.

**Bir payı bir paydaya bölmeden önce "bu ikisi AYNI zaman penceresinden mi?" diye sor — modül doğru olsa bile girdiler ayrışırsa sonuç yalan olur.** Denk'in bütçe önerisi payı `giderToplami(ayBasi, aySonu)` (BU AYIN gideri, 1.732 ₺), paydayı ise ilk işlemden bugüne geçen günden (63) alıyordu. Günlük hız 27 ₺ hesaplandı, gerçeği ~192 ₺ idi → öneri **800 ₺** çıktı ve kullanıcı kabul eder etmez ekran **"Bütçen bitti"** dedi. Üstelik kartın kendi cümlesi de yalan oluyordu: *"Son 63 günde 1.732 ₺ harcadın"*. `ButceOnerisi` saf ve DOĞRUYDU; 30+ testi vardı; hata hiç test edilmeyen **çağrı yerindeydi** — iki farklı pencereden gelen iki rakamı birleştirmek. Ürünün en önemli vaadi ("30 gün ölçer, kendi rakamını önerir") bu yüzden bozuktu ve ancak **mağaza görseli çekilirken gerçek veriyle** görüldü. Kural: saf modülü test etmek yetmez, GİRDİLERİN aynı pencereden geldiğini de kilitle (#28/#40/#59'un dördüncü tekrarı — bu depoda en sık tekrar eden hata sınıfı). YAN DERS: **mağaza/tanıtım görseli üretmek bir DENETİM aracıdır** — ürünü gerçek veriyle, kullanıcının göreceği hâliyle bakmaya zorlar.

---
*Kaynak: Denk bütçe önerisi 2026-08-09 → AnaEkranActivity.oneri + ButceOnerisiPencereTest*
