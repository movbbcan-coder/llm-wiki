---
ureten: hafiza-yayinla
tip: ders
no: 60
etiketler: [ders, rulebook]
---

# Ders 60 — Bir ürünün en güçlü iddiası, ölçülmemişse en büyük riskidir — izin/veri iddiasını APK'nın KENDİSİNDEN doğrula.

**Bir ürünün en güçlü iddiası, ölçülmemişse en büyük riskidir — izin/veri iddiasını APK'nın KENDİSİNDEN doğrula.** Denk'in tüm gizlilik konumlandırması "INTERNET izni yok" üzerineydi; Ayarlar ekranı kullanıcıya bunu YAZIYORDU ve Play Veri Güvenliği formu "veri toplanmıyor" diye doldurulacaktı. `aapt2 dump permissions` release APK'da INTERNET + ACCESS_NETWORK_STATE gösterdi; `manifest-merger-*-report.txt` kaynağı verdi: `transport-backend-cct` ← ML Kit (fiş OCR, FAZ 2'de gömülü modelden Play-Services sürümüne geçilince girmiş). Google'ın kendi belgesi ML Kit'in teşhis verisi (cihaz modeli, paket/sürüm, gecikme, kurulum-başı kimlik) yolladığını ve **kapatma yolu olmadığını** söylüyor. Yani beyan aylardır yanlıştı ve kimse bakmamıştı (#41 ailesi: "testler yeşil" ≠ iddia doğru). **Kural: bir bağımlılık eklendiğinde/değiştirildiğinde birleşmiş manifesti oku; kullanıcıya söylenen her izin/gizlilik cümlesi paketlenmiş çıktıdan doğrulanmalı. Doğrulanamayan iddia metinden ÇIKARILIR** (Denk'te çözüm: özelliği opt-in yap + ne gidip ne gitmediğini ayrı ayrı yaz). YAN DERS: `billing-ktx` Kotlin 2.2 ile derlenmiş, proje 2.0.21 → ksp patlar; Java artefaktı temiz, sarmalayıcıyı elle yaz.

---
*Kaynak: Denk gizlilik iddiası 2026-07-29 → AndroidManifest + Ayarlar metni + Tercihler.fisOkumaAcik + PLAY_VERI_GUVENLIGI.md*
