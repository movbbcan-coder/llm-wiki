---
ureten: hafiza-yayinla
tip: ders
no: 80
etiketler: [ders, rulebook]
---

# Ders 80 — Bir kanalın koptuğunu haber veren mesaj, o kanala emanet edilemez — ve tek bildirim kanalı SESSİZCE ölebilir.

**Bir kanalın koptuğunu haber veren mesaj, o kanala emanet edilemez — ve tek bildirim kanalı SESSİZCE ölebilir.** ccoto'da telefon tüneli koptuğunda kullanıcıya haber veren nöbetçi yazıldı; haber ntfy'e gönderildi ve kanalda göründü (`ntfy.sh/<topic>/json?poll=1` ile doğrulandı) ama **telefona ulaşmadı**: `dumpsys activity services io.heckel.ntfy` = **0**, Samsung pil eniyilemesi ntfy'nin arka plan servisini öldürmüştü. Yani "gönderdim" ile "ulaştı" arasındaki fark, tam da uyarı sisteminin işe yaraması gereken anda ortaya çıkıyordu. Fix: **iki bağımsız kanal** (ntfy + Telegram botu), her ikisi de HER SEFERİNDE denenir (kısa devre yok — "biri başarılıysa ötekini atla" ikinci kanalı sessizce çürütür), biri ulaşırsa haber verilmiş sayılır; canlı kanıt telefonun bildirim dökümünden alındı. YAN DERSLER (ikisi de aynı turda, "koruyucunun kendisi sessizce arızalanır" sınıfı): (a) nöbetçi, gönderim başarısız olsa bile "haber verdim" sayıp 30 dk'lık soğumayı başlatıyordu → **gönderimin gerçekleştiği ölçülmeden soğuma başlatılmaz**; (b) "son haber zamanı" sentinel'i `0.0` idi, yani "hiç gönderilmedi" ile "çok eskiden gönderildi" aynı sayıyla temsil ediliyordu → `None` yapıldı (#34'ün birebir tekrarı: bilinmeyen bir değer değildir). Ayrıca sağlık ölçümü SALT-OKUNUR tutuldu: mevcut `tel -c` aracı zombi oturum öldürüyor; **ölçmek ile müdahale etmek ayrı kararlardır** ve bir nöbetçi kendi başına yan etki üretmemelidir.

---
*Kaynak: ccoto F3.4 tünel nöbetçisi 2026-08-13 → backend/ccoto/tunel.py + http_api._tunel_nobetcisi + tests/test_tunel.py (13)*
