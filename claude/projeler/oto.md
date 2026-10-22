---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

## 2026-10-22 — Öğrenci paneli genişletilebilir menü (Codex)

Kullanıcı Movmain bot kimliğini yeniden kullanmayı ve günlük öğrenci işlerinin
menüsünü genişletmeyi onayladı. `backend/ccoto/universite_menu.py`: 7 bölüm,
27 işlem, tüm etiket/callback eşleşmeleri tek katalogda; Telegram'dan bağımsız
ekran üretimi ve yalnız yetkili özel sohbet erişim kapısı. Yeni bölüm/işlem aynı
kataloğa eklenebilir; her bölümün geri/ana menü yolu var. Canlı veri bağlanmadan
işlem ekranı açıkça güncel bilgi alınmadığını söyler; başarı, güncel not, derslik
veya mezuniyet koşulu uydurmaz. Ders kaydı, ödeme ve belge talebi gönderilmez.

Hedefli test: `tests/test_universite_menu.py` 14/14 (0.29 sn); kod benzersizliği,
64 bayt callback sınırı, bütün menü geçişleri, eski tuş ve yetkili özel sohbet
kontrolü. Bot servisine henüz bağlanmadı; Movmain güncel kodu/anahtarı doğrulanmadı.
Hotpeep başlatılmadı; mevcut CCOTO istemcisi değiştirilmedi. OBS ölçümü korunarak
bu adım tamamen çevrimdışı yapıldı. Sonraki kapı: Movmain kimlik doğrulama,
Telegram adaptörü ve test bittikten sonra her OBS menüsünün gerçek veri eşlemesi.
