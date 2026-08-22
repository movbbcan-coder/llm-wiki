---
ureten: hafiza-yayinla
tip: ders
no: 96
etiketler: [ders, rulebook]
---

# Ders 96 — Soğuma anahtarı DEĞİŞKEN içerikten türetilirse soğuma ölür — ve ölü soğuma "ayar var" diye görünmez kalır.

**Soğuma anahtarı DEĞİŞKEN içerikten türetilirse soğuma ölür — ve ölü soğuma "ayar var" diye görünmez kalır.** Duo Sentinel'in alarm anahtarı `level + mesajın ilk 40 karakteri` idi; mesaj **fiyatı** taşıyordu (`<b>ADAUSDT</b>  0.217000\nFiyat 1sa'da…`). Fiyat her 30 sn'de değiştiği için her tick YENİ anahtar doğuyor, `DUO_ALERT_COOLDOWN_SEC=900` hiçbir zaman tetiklenmiyordu. Canlı kanıt tek bakışta geldi: alarm damgaları 08:13:04 · 08:13:34 · 08:14:04 · 08:14:35 — tam 30 sn aralık, yani ayarlanan 900 sn'nin 1/30'u. **Ayarın VARLIĞI çalıştığının kanıtı değildir; anahtarın neyden türediğini oku.** İKİNCİ ve daha derin kusur: alarmın öncülü çökmüştü — `position: None`, `used_margin: 0`, yani izlenecek pozisyon YOKTU. Fiyat düşüşü alıcının yapabileceği hiçbir şeye bağlı değildi ve mesaj bunu kendi içinde SÖYLÜYORDU (`LIVE avg: —`), kimse okumadı (#90 birebir: "bunu alan kişi şu an ne yapacak?" cevabı "hiçbir şey" ise o bildirim yoktur). Fix üç kapı: (a) soğuma anahtarı alarmın TİPİ (`fiyat_dusus_1h`), metni değil — `kind` parametresi varsayılansız, unutulursa çağrı hata verir; (b) merdiven 30dk→2sa→8sa→24sa, koşul düşünce sayaç sıfırlanır (#82); (c) pozisyon yoksa fiyat alarmı gönderilmez, ama "ölçemedim" AYRI hâl — kör hesapta pozisyon olabileceği için hüküm kurulmaz, alarm geçer ve körlük mesajda isimlendirilir (#34/#35). Doğrulama biçimi: 4 mutasyon (kapıyı aç · merdiveni düzleştir · körlüğü "yok" say · None sentinelini 0.0'a düşür) tek tek uygulandı, dördü de testi kırdı; ayrıca kapı CANLI snapshot'la üç vakada ölçüldü (pozisyon yok→susar, pozisyon eklenince→konuşur, hesap okunamayınca→konuşur+isimlendirir) — restart sonrası fiyat geçmişi boş olduğu için "alarm gelmedi" gözlemi kapıyı KANITLAMAZDI (#94: guard'ı pozitif vakayla da sına).

---
*Kaynak: Duo Sentinel 30 sn'de bir ADAUSDT alarmı 2026-08-22 → duo/alarm_karar.py (saf çekirdek) + alerter.send_alert(kind) + price_watcher öncül kapısı + state.alert_tekrar + tests/test_duo_alarm.py (15)*
