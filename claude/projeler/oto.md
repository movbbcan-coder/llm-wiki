---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

##2026-10-25 — Sonraki oturum için kalıcı deney hazır (Codex; canlı WAITING)

Kullanıcı giriş yapmadan önce oturum loglarının geliştirilmesini, sonraki
kapanışta süre/VNC-restart etkisinin kanıtla ayrılmasını istedi. Sahip Codex.
İzole kopya `.work-session-trace.gyrd6bk0`; kendi basit API/işçi mimarisi korundu.
Yeni `session_trace.py` kalıcı runs/events/samples, `session_probe.py` sırsız
yerel /proc+pasif CDP gözlemi. Store şeması additive; Service yalnız gerçek
fetch sonuçlarını kaydeder. Mevcut worker60sn yerel tick'i gece de yürütür;
OBS'ye ilave istek, yenileme veya yeni timer/servis yoktur. İnsan önceliği
korunur, gözlem kilidi alınamazsa boşluk raporlanır. PID+start tick+engine,
boot/monotonik saat, VNC izleyici değişimi, görünür giriş ekranı ve hata
sınıfları kaydedilir. Cookie/şifre/token/HTML/IP/tuş kaydı yoktur.

Başlangıç ilk yeni OK/EMPTY live ve cached false doğrulamadır; eski metadata
ve önbellek deneye taşınmaz. Kapanış ilk yeni AUTH_REQUIRED sonucudur; ağ,
browser erişimsizliği, görünür HTML veya ekran yedeği kapanma diye yazılmaz.
Kaynak AUTH sonucu her zaman yeni401 değildir; kanıt adı AUTH_REQUIRED_RETURNED.
Son başarı–ilk auth aralığı, tek giriş varsayımındaki doğrulama süresi, ilk
giriş ekranı, restart/boşluk/olası yeniden giriş ayrı raporlanır. Saat oynaması
ve boot değişiminde süreye yanlış kesinlik verilmez. Görülmeyen yeniden giriş
olmayacağı deney varsayımıdır. Mevcut saatlik08–22 istekler devam ettiği için
bu saf idle TTL ölçümü değildir; gece gerçek süre aralığı geniş kalabilir.

Özet Ayarlar/Oturum'da ve sonraki gerçek tek kapanış uyarısında gösterilir;
spam veya yeni mesaj çizelgesi eklenmedi. Tek deney kapanınca örnekleme durur;
yeniden arm geçmişi silmez ve aktif deneyi sıfırlamayı reddeder.

Test511→537/537 (26 yeni),21,33s,6 eski uyarı; ağ kapalı/root salt okunur.
Host provider üç gerçek birimi ve giriş ekranını gördü. Geçişte yalnız bot
restart edildi; browser/VNC değişmedi. Son özel kod/DB yedeği
`veri/universite/releases/session-trace-20261024T215122Z`. Son bot1783459
active/NRestarts0; browser1473049 (eski NRestarts1), VNC1472624 aynı.25.10
00:51:26 İstanbul arm; WAITING, run0, yerel heartbeat ilerliyor. Önce/sonra
OBS fetch95→95, yapay test mesajı0; kullanıcı henüz yeni giriş yapmadı.
Tüm staged sürüm hashleri doğrulandı. Aktif deneye giriş için kullanıcıya
VNC + Telegram Girişi tamamladım/doğrula yolu verilecek; başka cihazdan yeni
giriş yapmadan normal kullanım istenir. Sonuç/TTL henüz varmış gibi raporlanmaz.

Tam protokol/sınırlar/geri dönüş: `.work-session-trace.gyrd6bk0/docs/SESSION_EXPERIMENT.md`;
canlı kanıt `docs/DEPLOY_RESULT.json`, test `docs/TEST_RESULTS.txt`.

##2026-10-25 — OBS oturum süresi salt okunur inceleme (Codex)

Kullanıcının24 Ekim giriş uyarısı sorusu üzerine canlı SQLite metrics/metadata,
Tracker sözleşmesi ve systemd/journal karşılaştırıldı.5 kapanma gözlemi var;
hepsi NOT_EXACT_EXPIRY. Son oturum24.10 02:39:20 ilk,02:39:56 son başarılı
okuma;08:00:26 AUTH_REQUIRED tespiti.5sa21dk06sn gerçek TTL değil, gözlem üst
sınırı; arada5sa20dk ara doğrulama yok. Gece rutin kontrol08'e kadar duruyor.

Önemli ek kanıt:24.10 06:08:20–24 bot/browser/VNC normal şekilde durdurulmuş
ve başlatılmış; browser ilk başlatma başarısız,06:08:40 tekrar ayağa kalkmış
(NRestarts1). Bu nedenle son kapanma otomatik OBS süresine bağlanamaz; tarayıcı
yaşam döngüsü etkisi karışıyor. Kim/ne durdurdu bu dar log kesitinden bilinmiyor.
Host uptime Haziran'dan beri; VPS reboot iddiası yok. Kod, oturum, servis ve
bildirim düzeni değiştirilmedi; OBS'ye istek veya Telegram mesajı gönderilmedi.
Tam5 dönem tablosu ve sınırlar: `docs/SESSION_AUDIT_2026-10-25.md`.

## 2026-10-23 — Tek seferlik duyurular + Telegram tam metin (Codex; canlı)

Sahip Codex. Kullanıcı genel duyuruların kaçırılmamasını, ders dışı olanların
bir kere bildirilmesini istedi. Gösterilen duyuru canlı DOM'dan doğrulandı:
26–30 Ekim Ayazağa–Maslak derslerinin çevrim içi yapılması; kullanıcıya kişisel
uygunluk çıkarılmadı. Genel Duyurular → Tüm Duyurular listesi ve detay şeması
normal menüyle doğrulandı. Öğretim elemanı mesajları açılmadı; genel Göster
işlemi site davranışı olarak okundu işaretleyebilir, okunma durumu dedup için
kullanılmaz. Snapshot kimlik/başlık/tarih/metin saklar; gönderen ve gizli alan yok.

`announcements.py` saf parser/kimlik/kural, `resources` gözlenen tek yeni kaynak,
`reader` arşiv/detay okuması, `store` ilk güncel duyuru yakalama, V2 kalıcı olay
ve Telegram kart/detay sayfaları eklendi. Yeni servis/zamanlayıcı yok. Ayarlar
→ Duyurular'da özet ve tam metin okunur; normal akademik ekranlarda web URL0.
Genel duyuru bir kez; sıra, okunma veya arşivden geri gelme tekrar üretmez.
Akademik gerçek içerik değişikliği yeni sürüm olabilir. İlk arşiv son7 gün/
yakın gelecekte açık akademik tarih ile daraltılır; eski arşiv topluca gönderilmez.
Kaynak cümlesi seçilir, yer/tarih/kişisel uygunluk uydurulmaz. Ek dosya açılmaz.

Canlı9 metin6,72s'de OK/live; Notlar→Duyurular tekrarı6,35s. HTTP yanıtı/iframe
DOM yarışı frame navigation olayıyla düzeltildi. İlk dağıtımdan sonraki taramada
geçici navigation Timeout gözlendi; aynı sırada tekrar edilemedi. Yanlış güncel
bildirim verilmedi. Bekleyen doğrulanmış bilgi taramadan önce gönderilir;
yalnız pending duyuru ağ hatasında mevcut işçi90sn arayla sınırlı tekrar yapar,
3 hatada durur. Auth/403/429/VNC/form korumaları aşılmaz. Arşiv45sn/3 sayfa
sınırını aşarsa kısmi başarı kabul edilmez; eski veri korunur.

Test493→511/511 (18 yeni),16,88s,6 eski uyarı; ağ kapalı/root salt okunur.
İki eski testin sabit kaynak/rota sayıları doğrulanmış yeni kaynak için uyarlandı.
Özel kod+DB yedeğiyle aynı bot güncellendi; son yedek
`veri/universite/releases/smart-ui-v2-20261023T153719Z`. Bot1271255 active,
NRestarts0; browser1171881/VNC594899 değişmedi. Son9 satır OK/live, bot kimliği
ve başlangıcı doğrulandı.2 güncel akademik duyuru tek728 karakter bildirimde
SENT; iki olay delivered, eski pending0. Yapay test mesajı yok.

Tam kanıt/sınırlar/geri dönüş: `.work-smart-ui-v2.bbDCir/docs/ANNOUNCEMENTS_DEPLOYED.md`.
Normal saatlik08–22 kontrol ve açık oturum şartı geçerlidir; fiziksel telefonda
tüm detay sayfalarının görsel kabulü yapılmadı. Yeni duyuru kaynağı artık canlıdır.
