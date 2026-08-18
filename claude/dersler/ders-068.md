---
ureten: hafiza-yayinla
tip: ders
no: 68
etiketler: [ders, rulebook]
---

# Ders 68 — "Uygulama ön plandan düştü" belirtisi çoğu zaman odak çalınması DEĞİL, ÇÖKMEDİR — Android çökünce önceki uygulamaya döner.

**"Uygulama ön plandan düştü" belirtisi çoğu zaman odak çalınması DEĞİL, ÇÖKMEDİR — Android çökünce önceki uygulamaya döner.** Denk'in yedeğini cihazda ölçerken ekran sürekli Termux'a dönüyordu; üç tur suç Termux'a, MacroDroid'e ve kendi çağrı hook'larımıza (`telmod` bayrağı AÇIKTI, hepsi susuyordu) atıldı. `adb logcat -b events \| grep am_crash` tek bakışta söyledi: `IllegalArgumentException: Failed to find configured root that contains .../cache/yedek/...denkyedek` — FAZ 0'da eklenen yedek klasörü `paylasim_yollari.xml`'e yazılmamıştı, `FileProvider.getUriForFile` paylaşım anında patlıyordu. **188 birim + 24 Paparazzi testi YEŞİLDİ** (FileProvider yalnız gerçek Android'de çözümlenir) — #63'ün birebir tekrarı. Fix: XML satırı + `PaylasimYoluTest` (FileProvider kullanan her adapter'ın `DIZIN` sabiti XML'de kayıtlı mı; sayıyı değil EŞLEŞMEYİ kilitler, satır kaldırılınca kırmızıya döndüğü ölçüldü). İKİNCİ ders: cihaz otomasyonunda **komut onayı istemek otomasyonu devirir** — kullanıcı onay için Termux'a döner, sürülen uygulama arkaya düşer, sonraki `input tap` Termux'a gider (bir kez parola metni kullanıcının prompt satırına yazıldı). Telefon komutlarını önceden `permissions.allow`'a ekle ve onay yüzeyini teke indir (`scp` yerine tek `ssh` + `adb exec-out base64`).

---
*Kaynak: Denk yedek paylaşımı cihazda çöktü 2026-08-09 → paylasim_yollari.xml + PaylasimYoluTest + settings.json allow*
