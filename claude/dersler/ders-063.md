---
ureten: hafiza-yayinla
tip: ders
no: 63
etiketler: [ders, rulebook]
---

# Ders 63 — "Testler yeşil" ≠ "uygulama açılıyor". Bir istemciyi GERÇEK cihazda çalıştırmadan "bitti" deme.

**"Testler yeşil" ≠ "uygulama açılıyor". Bir istemciyi GERÇEK cihazda çalıştırmadan "bitti" deme.** Denk 10 gündür HER AÇILIŞTA çöküyordu: Play Billing 8.x `PendingPurchasesParams`'ta `enableOneTimeProducts()` istiyor, yoktu → `IllegalArgumentException` Compose derlemesinde patlıyor, ana ekran hiç çizilmeden kapanıyor. O sırada **188 birim testi yeşildi ve 24 ekran Paparazzi ile render ediliyordu.** İkisi de yakalayamaz: Paparazzi bileşenleri YALITILMIŞ render eder (`Fatura` hiç kurulmaz), birim testlerinde Play Billing yok. Yani bütün doğrulama altyapısı "bu ekran nasıl görünür"ü ölçüyordu, "uygulama açılıyor mu"yu DEĞİL. İlk gerçek açılışta 10 dakikada çıktı. **Kural: her istemci projesinde "gerçek cihazda aç ve bir ekran görüntüsü al" bir KAPI olmalı; render testi onun yerine geçmez.** Kurulum bir kez yapılır, sonrası ucuz (bkz. `/root/bin/tel`, `telss`). YAN DERS: aynı turda projenin kendi risk defterinde ("`turetilmisBakiye` transferin iki bacağını da artı sayıyor") yazılı bir hata ölçülerek YENİDEN keşfedildi — **işe başlamadan projenin DEVAM/risk dosyasını oku**, tahminle değil kayıtla başla.

---
*Kaynak: Denk açılışta çökme 2026-08-09 → DEVAM.md "önce riskleri oku" notu + tel/telss araçları*
