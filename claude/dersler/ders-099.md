---
ureten: hafiza-yayinla
tip: ders
no: 99
etiketler: [ders, rulebook]
---

# Ders 99 — İki servis aynı tek-yazıcılı kaynağı paylaşırsa yarışırlar; kaybeden sonsuz restart'a girer ve kullanıcı ALARMDAN bunalır — ama asıl soru "yarışılan şey neye yarıyordu?"dur.

**İki servis aynı tek-yazıcılı kaynağı paylaşırsa yarışırlar; kaybeden sonsuz restart'a girer ve kullanıcı ALARMDAN bunalır — ama asıl soru "yarışılan şey neye yarıyordu?"dur.** `global-jobs-listener` **1585 kez** yeniden başlamış ve kullanıcıya aralıksız bildirim gitmişti. Hata logu boş görünüyordu çünkü PM2 kayıt yolu farklıydı (`pm2 describe` → `/var/log/global_jobs_listener_err.log`); gerçek sebep oradaydı: `sqlite3.OperationalError: database is locked`. Kilidi `fuser`/`lsof` ile tutan süreç bulundu: **sender.py**, Telethon istemcisini bir kez açıp (`_telegram_client` global) `disconnect` etmediği için `sessions/dubai_jobs_session` dosyasını süreç boyunca tutuyordu. Telethon oturumu SQLite'tır: tek yazıcı. Kim önce kaparsa o çalışıyordu (OOM sonrası `pm2 resurrect` sırayı değiştirince listener kaybetti). **Kritik adım tamir değil ÖLÇÜMDÜ:** yarışılan yolun log sayımı → başarılı DM **0** · başarılı kanal yanıtı **4** · başarısız **21.257** (%0,02). Telegram soğuk DM'i ("You can't write in this chat") ve kanal yanıtını ("Chat admin privileges are required") politika gereği engelliyor; sender'ın ÇALIŞAN kanalları e-posta ve WhatsApp, kullanıcı bildirimi ise Bot API (oturum gerektirmez). Yani **çalışmayan bir yol, çalışan bir servisi öldürüyordu**. Fix: `TG_SEND_ENABLED` (varsayılan **false**) — kapı, istemci açılmadan ÖNCE ve HER İKİ gönderim yolunda; Bot API bildirimi bayraktan etkilenmez. Kural: **paylaşılan tek-yazıcılı kaynağın (session dosyası, kilit, port, cihaz) tek bir sahibi ilan edilmeli**; ikinci tüketici ya kuyruk üzerinden geçer ya hiç dokunmaz. TEŞHİS SIRASI: `pm2 describe` (gerçek log yolu!) → err log → `fuser -v <dosya>` (kilidi kim tutuyor) → o sürecin kaynağında `disconnect` var mı → **yarışılan işlevin başarı oranını say**.

---
*Kaynak: dubai_jobs oturum yarışı 2026-08-25 → sender.TG_SEND_ENABLED + tests/test_oturum_tekil.py (4, iki mutasyonla doğrulandı)*
