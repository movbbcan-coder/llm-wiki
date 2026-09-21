---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

## 2026-09-21 14:24 TRT — İşCep hareket ekranı olay köprüsü canlıda

`TelefonErisimServisi`, yalnız İşCep kökünde dört hareket başlığı birlikteyse
60 saniye soğumalı `iscep_hareketler` olayı üretiyor; olay tutar/bakiye/IBAN/
açıklama taşımıyor. `Api.telefonOlay` → yetkili `POST /telefon/olay` → yeni
`backend/ccoto/telefon_olay.py` beyaz listesi → P2P loopback ucu. İç P2P sırrı
APK'ya verilmedi. Yeni APK derlendi ve cihazdaki MD5 `dcfc705d0682…` ile yerel
APK eşleşti; çökme kaydı yok. Kullanıcı hareket ekranını açınca olay otomatik
ulaştı ve P2P 4/4 eşleşme, 0 teyitsiz sonucu üretti. `tests/tumu.sh` tamamen
yeşil; Python 124/124, canlı API yetki kapısı 17/17. `ccoto-api` online.
