---
title: Bybit P2P Otomasyon Botu
date: 2026-04-13
tags: [bireysel, trading, telegram, bybit, p2p]
domain: bireysel
---

# Bybit P2P Otomasyon Botu

- **PM2 adı:** `bybit_p2p`
- **Script:** `/root/bireysel/bybit_zerinde_p2p_sat_lar_i/bot.py`
- **Durum:** ✅ Production (online, izleme aktif)
- **Son güncelleme:** 2026-04-13

## Amaç

Bybit P2P platformunda USDT satışlarını otomatize et:
- Zarara satmayı önle (maliyet bazlı min fiyat)
- Müşterilere otomatik banka bilgisi gönder
- Dekontları Gemini Vision ile doğrula
- Banka günlük limitlerini takip et ve otomatik rotasyon yap

## Özellikler

| Özellik | Durum |
|---|---|
| Bybit V5 API + HMAC imzalama | ✅ |
| Piyasa fiyat takibi (TRY + AED) | ✅ |
| İlan oluşturma / güncelleme | ✅ |
| Sipariş takibi 7/24 | ✅ |
| Banka yönetimi (Garanti/Enpara/ADCB) | ✅ |
| Maliyet havuzu + ortalama maliyet | ✅ |
| Min satış fiyatı koruması (%2 kar) | ✅ |
| Otomatik müşteri mesajı | ✅ |
| USDT serbest bırakma | ✅ |
| Dekont analizi (Gemini Vision) | ✅ |
| State persistence (restart-safe) | ✅ |
| Auto-start izleme | ✅ |
| Günlük rapor (22:00) | ✅ |

## Mimari

```
bot.py (monolith, ~900 satır)
├── Bybit API (HMAC, V5 endpoints)
├── State yönetimi (RAM + JSON persist)
├── Telegram bot (python-telegram-bot)
│   ├── ConversationHandler: maliyet girişi
│   ├── ConversationHandler: ilan oluşturma
│   └── CallbackQueryHandler: inline butonlar
├── İzleme döngüsü (60s)
│   ├── Sipariş kontrolü
│   ├── Fiyat uyarısı
│   └── Banka limit uyarısı
└── Günlük rapor (22:00 scheduler)

dekont_agent.py
└── Gemini Vision API ile dekont doğrulama
```

## State Dosyası

`/root/bireysel/bybit_zerinde_p2p_sat_lar_i/runtime_state.json`

Restart-safe veriler:
- `maliyet_havuzu` — USDT alım maliyetleri
- `gunluk_satis` — Bugünkü tamamlanan satışlar
- `aktif_siparis` — Açık siparişler
- `banka_kullanim` — Günlük banka kullanımı

## Bankalar

| Banka | Para | Günlük Limit |
|---|---|---|
| Garanti | TRY | 15,000 ₺ |
| Enpara | TRY | 25,000 ₺ |
| ADCB | AED | Limitsiz |

## Testler

`tests/test_bot.py` — 16 test, IO-bağımsız unit testler:
- Maliyet hesaplama (ağırlıklı ortalama)
- Banka seçimi (limit/durum kontrolü)
- State persistence (kaydet/yükle/hata)
- Dekont agent (typo kontrolü, onay mantığı)
- Piyasa fiyatı fonksiyonları

## Bilinen Limitler

- İzleme döngüsü RAM'de — process çökerse `izleme_aktif` False'a dönüyor (auto-start bu sorunu çözdü)
- Bybit P2P API testnet'i yok — gerçek API ile test edildi
- `siparis_listesi()` senkron — ileride async'e taşınabilir

← [[PROJELER_HUB]]
