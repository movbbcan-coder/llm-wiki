---
ureten: hafiza-yayinla
tip: ders
no: 71
etiketler: [ders, rulebook]
---

# Ders 71 — Ekranda cümle kuran kod, "bilinmiyor"u sıfıra çevirmesin — imza `Long?` olmalı, çağrı yerinde `?: 0L` DEĞİL.

**Ekranda cümle kuran kod, "bilinmiyor"u sıfıra çevirmesin — imza `Long?` olmalı, çağrı yerinde `?: 0L` DEĞİL.** Denk'te kredi kartı satırı, çıpası olmadığı için bakiyesi BİLİNMEYEN karta **"borcun yok"** diyordu; oysa kartta 3,49 ₺ harcama vardı. Sebep: `KartDonemi.not(... borcKurus: Long)` null kabul etmiyordu, çağrı yeri `(bakiye as? Bilinen)?.kurus ?: 0L` ile bilinmeyeni sıfıra düzleştiriyordu — ve `borcKurus <= 0 → "borcun yok"` dalı yanlış cümleyi kuruyordu. **190 birim testi bunu göremezdi: testlerin hepsi 0'ı AÇIKÇA geçiyordu, yani "bilinmeyen" hâl hiç kurulmuyordu** (rulebook #34'ün tekrarı + #63'ün kanıtı: hatayı cihaz kapısı yakaladı, süit değil). Kural: bir değer "yok/0" ile "bilinmiyor"u ayırt etmek zorundaysa bu ayrım TİPTE yaşamalı; `?: 0L` gördüğün her yerde "burada sıfır mı demek istiyorum, bilmiyorum mu?" diye sor. YAN DERS: `uiautomator dump` ekran geçişi sırasında BAYAT ağaç döndürüyor (döküm Ayarlar dedi, ekranda kart çıpası vardı) → şüphede ekran görüntüsü al; döküm hızlı, görüntü doğru.

---
*Kaynak: Denk KARAR FAZ 1 kart borcu 2026-08-09 → KartDonemi.not(Long?) + test + HesaplarimEkrani*
