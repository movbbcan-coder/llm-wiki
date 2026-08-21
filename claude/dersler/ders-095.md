---
ureten: hafiza-yayinla
tip: ders
no: 95
etiketler: [ders, rulebook]
---

# Ders 95 — Sahiplik sorusunda "nerede duruyor" ile "kim kullanıyor" ayrı şeylerdir; ikisi de tek başına yanlış cevap verir.

**Sahiplik sorusunda "nerede duruyor" ile "kim kullanıyor" ayrı şeylerdir; ikisi de tek başına yanlış cevap verir.** Telegram bot envanteri üç kez yazıldı: (v1) token'ı **bulunduğu ilk dosyaya** göre projeye atadı → `/root/.env.bak` içindeki canlı botlar (`@Ccotobot`, `@ceobbcanbot`) ÖKSÜZ göründü; o liste uygulansaydı çalışan ccoto botu BotFather'dan silinecekti (ad geri gelmez). (v2) düzeltme sahipliği **değişken adından** çözdü → `TELEGRAM_TOKEN` 18 projede geçtiği için bu sefer HER ŞEY canlı göründü ve gerçek öksüzler kayboldu: bir yanlış öncülü düzeltirken karşıt hata üretildi. (v3) eşleşme token **DEĞERİ** üzerinden yapıldı + üç kanıt katmanı (A: çalışan sürecin ortam değişkeninde — ama yalnız 3/31 süreç token taşıyor, gerisi çalışırken .env okuyor; B: çalışan servisin proje dizininde; C: aktif genel `/root/.env` içinde) ve **kanıt yoksa "BELİRSİZ" denildi**. Tam da o kutuya düşen `@tm_vpn_mov_bot`'un PM2'si yoktu ama **cron'da 2 aktif işi** vardı — otomatik hüküm verilseydi kaybedilecekti. **Kural: geri alınamaz bir liste üretiyorsan (silinecekler) her satır hangi KANITA dayandığını taşımalı; kanıtsız satır silme listesine değil "elle bak" listesine gider.**

---
*Kaynak: VPS temizliği bot envanteri 2026-08-21 → /root/claude/telegram_bot_envanteri.md + bot_envanter3.py*
