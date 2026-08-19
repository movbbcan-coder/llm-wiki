---
ureten: hafiza-yayinla
tip: ders
no: 91
etiketler: [ders, rulebook]
---

# Ders 91 — "Makro/servis AÇIK" ile "tetikleyici ÇALIŞIYOR" ayrı şeylerdir — ve ölçüm aracının YETKİSİ ölçümün parçasıdır.

**"Makro/servis AÇIK" ile "tetikleyici ÇALIŞIYOR" ayrı şeylerdir — ve ölçüm aracının YETKİSİ ölçümün parçasıdır.** Banka bildirim hattı 13,7 gün (330 sa) ölüydü; nöbetçi (#84) doğru bağırıyordu ama arıza telefondaydı. Teşhis sırası işe yaradı: (a) nginx erişim logunda telefondan **hiç** istek yok — ne `/bildirim` ne 5 dk'da bir gelmesi gereken `/hb_sagligi`; (b) SSH tüneli de kapalı → üç kanal birden ölmüş = tek kök neden; (c) sunucu ucu elle test → HTTP 200, kayıt düştü (yani sunucu masum). Cihazda: MacroDroid **kurulu, açık, makro etkin, hedef URL doğru** — ama `enabled_notification_listeners` listesinde MacroDroid YOKTU (izin sessizce düşmüş; makro kartındaki "Son Aktivasyon: 6 Ağu" tam da hattın sustuğu gün). Fix: `adb shell cmd notification allow_listener <pkg>/<cls>` (sınıf adı `dumpsys package … | grep NotificationListener` ile ÖLÇÜLDÜ, tahmin edilmedi) + `appops … AUTO_REVOKE_PERMISSIONS_IF_UNUSED ignore`. **ÖLÇÜM TUZAĞI (asıl ders):** aynı `settings get secure enabled_notification_listeners` komutu Termux uid'siyle (10668) **boş** döndü — hata değil, sessiz boşluk — ve ben "hiçbir uygulamanın bildirim erişimi yok" diye yanlış teşhis kurdum; `adb shell` (uid 2000, WRITE_SECURE_SETTINGS) ile okuyunca liste 10 uygulamalıydı. **Bir cihazda ölçüm yaparken önce `id` çalıştır: hangi kimlikle okuduğunu bilmiyorsan okuduğun boşluk veriyi değil YETKİNİ ölçüyor olabilir** (#76 ailesi). YAN DERSLER: (1) `telss` çağrımda `-u` yalnız paket adı aldığı için `am start -n` hata verdi, `set -e` zinciri öldürdü, `rm`+`screencap` hiç koşmadı ve pull **15 saat önceki** dosyayı çekti → araç bayat ekranı taze diye sundu (#89'un tekrarı; fix: silme `set -e`'den ÖNCE + `am start` başarısızlığı ekran çekmeyi engellemesin); (2) MacroDroid'in "Makroyu test et" özelliği değişkenleri çözmeden gönderiyor (`app={not_app_name}`) — bu kayıt hattı CANLI saydırıp nöbetçiyi kendi doğrulama testimizle susturacaktı (#84'ün TEST_ONEK dersinin kardeşi, filtre eklendi).

---
*Kaynak: banka bildirim hattı 13,7 gün ölü 2026-08-19 → cihazda notification listener izni + appops + telss `set -e` sırası + bildirim_nobetci.COZULMEMIS_ISARET + test (18)*
