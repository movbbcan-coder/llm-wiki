---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

##2026-11-06 — Android read-only audit kurtarma ve rapor (Codex; PARTIAL)

Sunucu kesintisi sonrası4Kasım kaydedilmiş35 başarılı komut artefaktı bulundu;
ikinci/sorun örneği yok, son followup çağrısı başlamamış. Şimdi tel/SSH8022
connection refused(host doğrulaması da aynı); otomatik onarım/ayar yok.
Önceki kullanıcı ekranıyla mevcut eşleşmeye adb connect olmuş, pair kodu
kullanılmamış. CihazSM-S928B/Android17/API37; kullanıcı 'normal' demişti.
CPU normal örnekte çoğunlukla boşta; Input enabled/not frozen/queue empty,
68G disk boş. Vending/GMS PID/CPU/PSS ayrı eşlendi; paketli meminfo çağrısı
global döndüğünden heap dump iddiası yok. NotchTouch görünürtrusted overlay
NOT_TOUCHABLE tam ekran ve314x104 etkileşim alanı; suçlu ilan edilmedi.
Store güncelleme zamanı, çoklu profil/swap, hafifthermal ve gece Permission
Controller crash'i5düşük/orta güvenli hipotez olarak raporlandı. Arıza anı
yok; kök neden ve çözüm kanıtlanmadı. Gizlilikle arındırılmış rapor tek kaynak:
`bulgular/android-readonly-20261104/RAPOR.md`. Ham dosyalar özel yerel700/600;
uygulama/izin/veri/ayar/cihaz restartı değişmedi. Sonraki adım mevcut erişim
yeniden gelince aynı komutlarla gerçek sorun+normal kısa örnek karşılaştırması.

##2026-11-04 — Telefon kasma/Play Store read-only teşhis: ADB yok

Kullanıcı kesin salt-okunur sınırla CPU/RAM/ANR/thermal/input/overlay audit
istedi. SSH/Termux ulaşılabilir, doğrudan adb devices -l exit0 fakat liste boş.
tel -a devices ilk denemesi boş cihaz seçimiyle help döndürdü; ADB client
Termux server'ını otomatik açtı, Android cihaz/ayar/uygulama değiştirilmedi.
Onarım/tel -c/settings put/connect/pair çalıştırılmadı. ADB shell olmadan
ölçüm ve5neden sıralaması kanıtsız olduğundan yapılmadı. Ayrıntı ve devam
koşulu `bulgular/android-readonly-20261104/README.md`; kullanıcı mevcut ADB
erişimini hazır edince cihazlistesiyle tekrar doğrula. Ham bugreport alınmadı.

## 2026-10-28 — Baloncuk/mesaj tasarımı0.3.3 ve kilit düzeltmesi (UI_PASS_AUTO_PENDING)

Kullanıcı kaybolma, okunabilir mesajlar ve taş figürü istedi; ayrıca şeffaf/tıklanamaz
baloncuğu ve hamleden sonra otomatik cevap gelmemesini bildirdi. Sahibim Codex.
Üç neden doğrulandı: dış dokunmada kapanma, global work-mode ile panelin kaybı,
15s sonra satranç cevabının normal akışla ezilmesi. Pinned satranç modu, stale-callback
koruması, geri açılma niyeti/taslak, sarılan kartlar ve SAN taş/isim/hedef gösterimi
eklendi.5 Android kaynak/test dosyası hash preflight sonrası kanoniğe uygulandı.
0.3.2 alpha0.35/NOT_TOUCHABLE kararı kullanıcıyı kilitledi; canlı window fl18 ile
doğrulandı.0.3.3 bu hatayı giderdi: giriş noktası opak/tıklanabilir; kullanıcı açtığı
paneli work-mode kapatamaz. Backend yetki/bot kapıları değişmedi.

Android15/15 test PASS,37s buildSUCCESS; önceki politika modelinde3 red kanıtı var.
APK0.3.3/versionCode5 kuruldu; aktarım/kurulu hash/açılış/çökme kapısı PASS. SHA256
e6119b0174e8d5a6572bb1b7fb47973e05f88f91faf2e3ebff18f931543a06ac. Gerçek cihazda
mode AÇIKKEN panel açıldı, düğme isteği gitti ve20s opak/görünür kaldı. Motor
mevcut ilerlemiş bot oyununa aday0/yasal zincir hatası döndürdü; analiz başarısı
iddia edilmedi. Otomatik hamle takibi HENÜZ YOK. İşin bu kısmı tamamlandı sayılmadı.

Kanıt/rollback SSOT `/root/oto/bulgular/bubble-ui-20261028/README.md`; yedekler
ve0.3.2 hata artefaktı korundu, uninstall/veri silme/servis restartı/push yapılmadı.
Etki aracı .kt desteklemedi; çağrılar elle ve test/derleme/cihazla doğrulandı.
Sonraki dar iş ve mevcut kullanıcı yetkisi taze /root/oto oturumu için kaydedildi:
`/root/oto/docs/DEVIR_20261028_SATRANC_OTOMATIK.md`. Bu tur yeni alt iş/ajan açılmadı.
