---
ureten: hafiza-yayinla
tip: ders
no: 25
etiketler: [ders, rulebook]
---

# Ders 25 — Telegram Mini App auth: bazı bot/kurulumlarda `tg.initData` VE `initDataUnsafe`

Telegram Mini App auth: bazı bot/kurulumlarda `tg.initData` VE `initDataUnsafe` **boş** gelir (TG=true, len=0) → HMAC doğrulaması hep 403. Kovalamak yerine **gizli anahtar** kullan: bot WebApp URL'ine `?k=SECRET` göm (initData fragment'te, k query'de korunur), frontend `location.search`'ten okuyup header'la yollar, backend `hmac.compare_digest`. initData gelirse o da kabul (çift yol). Ayrıca Telegram initData'ya yeni `signature` alanını ekledi → HMAC data_check_string'den `hash` İLE BİRLİKTE `signature` de çıkarılmalı

---
*Kaynak: bank/ceo Mini App "Yetkisiz erişim" 2026-06-17 → bank_app/api/app.py + ceo_hub/webapp.py*
