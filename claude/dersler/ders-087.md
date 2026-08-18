---
ureten: hafiza-yayinla
tip: ders
no: 87
etiketler: [ders, rulebook]
---

# Ders 87 — #52'nin İKİNCİ kurbanı: kullanıcı ayarı bu kez MİRASLA değil FORMÜLLE ezildi — `max(ayar, formül)` deseni ayarı sessizce geçersiz kılar.

**#52'nin İKİNCİ kurbanı: kullanıcı ayarı bu kez MİRASLA değil FORMÜLLE ezildi — `max(ayar, formül)` deseni ayarı sessizce geçersiz kılar.** Ekran "min sipariş 1.000–6.000 ₺" derken canlı Bybit ilanı **1.185,25 ₺** ile açılmıştı; kullanıcı tutarsızlığı gördü ve sordu. Sebep: BW ilan oluştururken `min_try = max(_etkin_min_sip(...), bakiye × min_order_pct × fiyat)` hesaplıyordu — 431 USDT × %5 × 55 = 1.185,25 ve kullanıcının 1.000 ₺ ayarını EZDİ. İki ayrı zarar: (a) ekran ile gerçek ilan ayrıştı (kullanıcı hangisine inanacağını bilemez), (b) medyan sipariş ~600 ₺ olan bir piyasada min sessizce yukarı itilince hedef alıcı kitlesi ilanı hiç GÖREMEZ — yani gelir kaybı ölçülemeden oluşur. Üstelik bu depoda min/max için 2026-07-31'de `trading/ilan_limit` SSOT'u kurulmuştu; BW o göçe DAHİL EDİLMEMİŞTİ (yarım göç, #45). **Kural: bir alan kullanıcı ayarıysa formül onunla YARIŞAMAZ; `max(ayar, hesap)` / `min(ayar, hesap)` desenleri gördüğünde "bu alanın sahibi kim?" diye sor — sahibi kullanıcıysa hesap yalnız ayar YOKKEN devreye girer.** Doğrulama biçimi de dersti: hatayı ne test ne log yakaladı, **ekranda gösterilen sayı ile dış dünyadaki (Bybit) sayının kıyaslanması** yakaladı (#41: ekran ↔ bağımsız dış kanıt mutabakatı).

---
*Kaynak: BW min sipariş 1.185,25 vs ayar 1.000 · 2026-08-18 → dongu_bakiye min_order_pct formülü kaldırıldı + test_bw.TestMinKullaniciAyari (5)*
