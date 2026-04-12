---
title: AXIOM CEO Bot — Sistem Durumu ve Tamir Planı
date: 2026-04-12
tags: [axiom, ceo-bot, mimari, tamir, refactoring]
sources: []
---

# AXIOM CEO Bot — Sistem Durumu

## Genel Hedef
VPS üzerinde çalışan otonom CEO botu. Telegram üzerinden komut alır, proje üretir, deploy eder.
Kalite hedefi: 90/100 (başlangıç: 52/100)

## Aktif Process'ler (PM2)
- `ceo_claude` (ID:35) — Ana bot — `/root/bireysel/main.py`
- `ceo_worker` (ID:36) — Ağır işler (CodeFactory, Kapıcı)
- `ceo_watchdog` (ID:37) — PM2 izleyici
- `ceo_obsidian_sync/indexer/change_watcher/daily_summary/weekly_report/decision_router` — Online

## Mimari (Mevcut)
```
Telegram → main.py (43 satır bootstrap)
              ↓
          bot/message_handler.py   ← mesaj routing
          bot/callback_handler.py  ← inline button routing
          bot/fabrika_handler.py   ← proje içi araçlar
              ↓
          bot/worker_queue.py      ← /tmp/ceo_queue.jsonl'e yaz
              ↓
          ceo_worker.py            ← queue oku, işle, TG'ye bildir
              ↓
          proje_fabrikasi/orchestrator.py  ← CodeFactory pipeline
          kapici/agent.py                  ← Fikir analizi
```

## Dosya Yapısı (Ana)
```
/root/bireysel/
├── main.py                    ← 43 satır bootstrap
├── config.py                  ← TOKEN, API_KEY, AUTHORIZED_USER_ID
├── ceo_worker.py              ← Worker process
├── ceo_watchdog.py            ← PM2 izleyici
├── bot/
│   ├── ai.py                  ← ai_route(), ai_cevap()
│   ├── projects.py            ← get_projects(), load/save_state(), pm2_status()
│   ├── keyboards.py           ← klavye(), proje_listesi_kb()
│   ├── ticker.py              ← cf_ticker() animasyonu
│   ├── worker_queue.py        ← queue_job(), worker_health()
│   ├── fabrika_handler.py     ← Proje araçları (Tahta, Deploy, SPEC, Git...)
│   ├── message_handler.py     ← on_message(), pending_action sistemi
│   └── callback_handler.py   ← on_callback()
├── kapici/
│   └── agent.py               ← donustur() → {metin, skorlar, sorular}
│                                 analyze() → sadece metin döndürür (metadata kaybolur!)
└── proje_fabrikasi/
    ├── orchestrator.py        ← CodeFactory.build_project()
    ├── models/unified_client.py ← OpenRouter multi-model client
    ├── fabrika.py             ← build_from_idea() (kullanılmıyor)
    ├── deployer.py            ← PM2 deploy
    └── project_tracker.py     ← SQLite CRUD
```

---

## Bu Session'da Yapılanlar (2026-04-12)

### ✅ Tamamlandı
1. **pending_action refactor** — 8 ayrı awaiting_* flag → tek `pending_action = {"type": "...", "data": {...}}`
   - Etkilenen: message_handler.py, callback_handler.py, fabrika_handler.py
2. **Worker heartbeat** — `/tmp/ceo_worker.heartbeat` her 2s'de yazılır
   - `worker_health()` fonksiyonu: PID + heartbeat yaşı → alive/dead
   - spec_start, gen_code, feat_gen callback'leri worker ölüyse uyarı verir
3. **_extract_files_from_spec() güçlendirildi**
   - Regex: .py/.json/.env/.sh/.md/.yaml destekler, alt klasör destekler
   - LLM fallback (Gemini Flash) → JSON array
   - Son çare: ["main.py", "config.py", "utils.py"]
   - SPEC prompt güncellendi: dosyaları backtick formatında ister

---

## Kalan Sorunlar ve Çözüm Planı

### SORUN 1: Çift Code Factory Yolu ⚠️ KRİTİK
**Durum:** `fabrika_handler.py → "🏭 SPEC"` butonu direkt `CodeFactory.build_project()` çağırıyor
(main thread'de, asyncio.to_thread ile ama yine de senkron).
Aynı zamanda `callback_handler.py → spec_start:` worker queue'ya gönderiyor.
**Çözüm:** "🏭 SPEC" butonu da worker queue'ya gönderilmeli. Direkt çağrı kaldırılmalı.
**Dosya:** `/root/bireysel/bot/fabrika_handler.py:184-220`

### SORUN 2: Worker Sonuçları Okunmuyor ⚠️ KRİTİK
**Durum:** Worker `ceo_results.jsonl`'e sonuç yazıyor ama bot hiç okumuyor.
Worker direkt Telegram API'yi çağırıyor (urllib.request) — bu geçici çözüm.
Bot restart'ta pending job'lar kaybolur.
**Çözüm:** Bot'a `JobQueue` ile 5s'de bir `ceo_results.jsonl` okuyan poller ekle.
Worker sonucu hem dosyaya yazsın hem TG'ye göndersin (çifte güvence).
**Dosya:** `main.py`'e scheduler job eklenecek

### SORUN 3: Kapıcı Metadata Kayboluyor ⚠️ ÖNEMLİ
**Durum:** `kapici.analyze()` sadece `donustur()["metin"]` döndürüyor.
Skor (idea_quality, completeness, execution_risk) ve sorular çöpe gidiyor.
**Çözüm:** `analyze()` yerine `donustur()` kullan. Skorları Telegram'a göster.
**Dosya:** `kapici/agent.py:344`, `bot/message_handler.py`

### SORUN 4: İki State Kaynağı ⚠️ ÖNEMLİ
**Durum:** `state.json` (her proje klasöründe) + `projects.db` (SQLite) — senkronize değil.
Proje fabrikası SQLite'ı güncelliyor, bot state.json okuyor.
**Çözüm:** Orta vadeli — state.json'u primary olarak tut, SQLite'ı mirror yap.
Ya da SQLite'ı kaldır, sadece state.json kullan.

### SORUN 5: pm2_status Her Çağrıda subprocess ⚠️ PERFORMANS
**Durum:** Her `pm2_status()` çağrısı `pm2 jlist` subprocess açıyor.
N proje için N subprocess = yavaş + CPU spike.
**Çözüm:** Cache ekle — 10 saniye TTL ile pm2 listesini belleğe al.
**Dosya:** `bot/projects.py:59`

### SORUN 6: state.json → SQLite Entegrasyonu (Orta Vadeli)
- Worker CodeFactory çıktılarını /root/bireysel/projeler/ altına kopyalıyor
- Ama state.json /root/bireysel/{proj_name}/ altında
- Bot get_projects() /root/bireysel/ altına bakıyor, /projeler/ değil
- Üretilen projeler görünmüyor olabilir

---

## Öncelik Sırası (Sonraki Session)
1. Çift CF yolu → tek yol (worker queue) [KRİTİK]
2. pm2_status cache [HIZLI, 10 dk]
3. Kapıcı metadata göster [ÖNEMLİ]
4. Worker result poller [ÖNEMLİ]
5. State/SQLite entegrasyon analizi [ORTA VADELİ]

---

## Model Seçimi
- Hızlı sorular: kimi-k2.5
- Derin analiz: deepseek-r1
- Kod üretimi: deepseek-chat-v3
- Router/planlama: gemini-2.0-flash
- Validation: qwen-2.5-72b

## Config
- Token: config.py → TELEGRAM_TOKEN
- API: config.py → OPENROUTER_API_KEY (sk-or-v1-7382ff...)
- Authorized: AUTHORIZED_USER_ID=5580093599
