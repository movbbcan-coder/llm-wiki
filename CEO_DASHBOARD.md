---
title: CEO Dashboard
date: 2026-04-13
tags: [ceo, dashboard, hub]
type: dashboard
---

# CEO DASHBOARD

> Merkez kontrol noktası. Buradan başla.

---

## 🚀 AKTİF PROJELER

| Proje | Domain | Durum | Sonraki Aksiyon |
|-------|--------|-------|-----------------|
| [[axiom-ceo-bot-durum\|CEO Bot]] | bireysel | 🟡 Tamir | Çift CF yolu → worker queue |
| [[reels_analizi\|Reels Analizi]] | bireysel | 🟢 Aktif | Faz 2 — analiz motoru |
| [[halka_arz_bot\|Halka Arz Bot]] | bireysel | 🟢 Aktif | 1 bekleyen görev |
| [[gsm_servis\|GSM Servis]] | ticari | 🟡 Beklemede | Tahta kur |

## 🕓 BEKLEYEN PROJELER

| Proje | Domain | Durum |
|-------|--------|-------|
| [[kilo_takip\|Kilo Takip]] | bireysel | ⏸ Faz 1 tamamlandı |
| [[kapici\|Kapıcı]] | bireysel | ⏸ Entegre (CEO Bot içinde) |

---

## 📋 SON KARARLAR

- [[kararlar/2026-04-13|2026-04-13]] — Wiki reorganizasyon
- [[kararlar/2026-04-12|2026-04-12]] — CEO Bot refactor
- [[kararlar/2026-04-11|2026-04-11]] — Sistem audit
- → [[KARARLAR_HUB|Tüm kararlar]]

---

## 🗂️ KATMANLAR

- [[PROJELER_HUB]] — Tüm projeler detay
- [[TECH_HUB]] — Teknik bilgi tabanı
- [[index|Wiki Index]] — Tam katalog

---

## ⚡ CEO BOT KRİTİK SORUNLAR

1. **Çift CF yolu** — KRİTİK → `fabrika_handler.py:184`
2. **Worker result okunmuyor** — KRİTİK → `main.py` poller ekle
3. **Kapıcı metadata kaybı** — `kapici/agent.py:344`
4. **İki state kaynağı** — `state.json` vs SQLite

Detay: [[axiom-ceo-bot-durum]]
