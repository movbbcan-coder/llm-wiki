---
ureten: hafiza-yayinla
tip: ders
no: 93
etiketler: [ders, rulebook]
---

# Ders 93 — Canlı akış panelinde içeriği tazelemek kaydırma konumunu sıfırlıyorsa, kullanıcı HER ZAMAN en eski satırı görür ve akışı "geride kalmış" sanır — veri güncel, GÖRÜNEN yer eskidir.

**Canlı akış panelinde içeriği tazelemek kaydırma konumunu sıfırlıyorsa, kullanıcı HER ZAMAN en eski satırı görür ve akışı "geride kalmış" sanır — veri güncel, GÖRÜNEN yer eskidir.** ccoto baloncuk paneli Claude'un canlı çıktısını 3 saniyede bir tazeliyordu; her tazelemede `TextView.text` yeniden yazılıyor ve ScrollView kaydırmayı en üste (yani gelen 40 satırın EN ESKİSİNE) sıfırlıyordu. Kullanıcının gördüğü: *"yazılar güncel yazıyı göstermiyor, iki üç mesaj geçmişi görüyorum; son yazdıklarına dönmek istediğimde otomatik eski metne atıyor."* Akış tamamen canlıydı — panel her 3 saniyede kullanıcıyı okuduğu yerden koparıp tepeye fırlatıyordu. **İki ayrı hata gibi görünen tek kök neden:** "geride kalmış içerik" ile "aşağı inince geri atıyor" aynı sıfırlamanın iki yüzü. Kural: canlı tazelenen bir görünümde içerik değişince kaydırma konumu KORUNUR; kullanıcı zaten en alttaysa (canlı takip ediyorsa) en alta yapışır, değilse okuduğu yerde kalır. Ayrıca metin DEĞİŞMEDİYSE hiç yazma — gereksiz layout hem kaydırmayı bozar hem o an süren bir dokunuşu iptal edebilir. YAN DERS (aynı turda, ölçüldü): **adb'nin sentetik dokunmaları (`input tap/swipe/motionevent`) `FLAG_NOT_FOCUSABLE` olan overlay penceresine ULAŞMIYOR** — ccoto baloncuğu böyle; panel penceresine (odaklanabilir) ulaşıyordu, klavye açıldı. Yani bir overlay'in dokunma davranışı otomatik test edilemiyorsa bu bir ürün kusuru değil, aracın sınırıdır: doğrulamayı gerçek parmakla yaptır, "çalışmıyor" diye kod arama.

---
*Kaynak: ccoto baloncuk paneli 2026-08-28 → Panel.akisiYaz kaydırma koruması + değişmediyse-yazma freni*
