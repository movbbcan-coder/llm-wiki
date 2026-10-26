---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

##2026-10-25 — E1 ilk sonuç: kapanış, ardından yeni başarı (Codex audit)

run2 başlangıç17:51:10, son başarı17:51:24 İstanbul. İlk E1 denemesi
18:37:05 (45dk40sn sonra),18:37:09 NETWORK_ERROR/navigation/Error;
18:38:09 ilk login_screen;18:51:20 AUTH_REQUIRED doğrulaması. Yaklaşık47dk
sonra giriş ekranı görüldü; bu süre gerçek geçerlilik/TTL değildir. Ara canlı
başarı yok; 45dk kontrolün oturumu yenilediği kanıtlanmadı.61 örnekte aynı
bot/browser/VNC kimlikleri; systemctl de restart olmadığını doğruluyor.
18:52:48 dersler OK/live + reauth CONFIRMED, güncel auth boş: uyarı sonrası
erişim tekrar doğrulanmış. Kimin/nasıl yeniden açtığı bu kayıtlardan bilinmez.
Yeni başarı CLOSED run2'yi otomatik yeniden açmaz; E1 maintain_session yalnız
ACTIVE run çalıştırdığından sonraki pilot için yeni ölçüm hazırlığı gerekir.
E2'ye geçmeden navigation hatasının dar, sırsız teşhisi ve kapanış sonrası
yeniden-deney akışı test edilmeli. Bu tur kod/servis/arm değiştirilmedi.

##2026-10-25 — E1 onaylı canlı geçiş (Codex; ACTIVE)

Kullanıcı açıkça onayladı ve giriş yapacağını bildirdi. BASELINE/RELEASE
hash kapıları geçti; iki dosya aynı bota aktarıldı. Özel kod+SQLite yedeği
`veri/universite/releases/session-e1-20261025T145037Z`; uygulama aracı
`.work-beykent-master-e1/deploy/apply_e1.py`, rollback kod+deney metadata
değerlerine döner, DB geçmişini geri sarmaz. E1 açık,17:51:07 İstanbul arm;
17:51:08 worker heartbeat ve bot kimliği doğrulandı. Bot2081831 active,
NRestarts0; browser1473049 ve VNC1472624 süreç/start kimlikleri değişmedi.
Yapay test mesajı0. Başlangıç WAITING sonrası yeni canlı başarı17:51:10
run2 ACTIVE oluşturdu;17:51:24 tekrar başarı, auth boş, login_pending no.
Eski run1 CLOSED korundu; eski başarı deneye taşınmadı. İlk E1 okuması
ACTIVE run'ın son başarısından45dk sonra; 7gün/24sa sonuç henüz yok.
Ürün testleri önceki adayda546/546; canlı hash doğrulandı. Materyal/mail
ve diğer envanter maddeleri sıradaki aşamalarda, tamamlandı sayılmadı.

##2026-10-25 — Ana protokol ve E1 aday uygulama (Codex; üretim onayı bekliyor)

SSOT `BEYKENT_MASTER_PLAN.md`: hipotez/eleme zinciri,7gün girişsiz kabul,
öğrenci ihtiyaçları audit listesi, onaylı belge/mail, test/yayın kapıları.
İzole `.work-beykent-master-e1` adayında Service.maintain_session ve mevcut
worker çağrısı hazır: E1 açık + ACTIVE trace ile45dk ders okuması, gece/bildirim
ayarından bağımsız; aynı okuyucu/kilit/form/VNC/cooldown kapıları korunur.
Kapalı auth veya kullanıcı önceliğinde istek yok; cache gerçek başarı sayılmaz.
Yeni servis/bağımlılık/bildirim yok.9 yeni test; son doğrulanmış537 testle
546/546 geçti22,58sn (ağ kapalı,root salt okunur),6 eski uyarı. İlk fixture
kopyası7 hata verdi; deploy dosyaları ve son release testleri tamamlandı,
ürün davranışı gevşetilmedi. İki dosya diff/hash ve geri dönüş planı
`.work-beykent-master-e1/docs/E1_RELEASE.md`. Canlı kod/metadata/servis
değişmedi, pilot başlamadı. Kullanıcının önceki üretim öncesi onay şartı gereği
sonraki adım kontrollü yayın onayı; materyal/mail genişletmeleri listede bekler.

##2026-10-25 — İlk kontrollü oturum sonucu (Codex; salt okunur denetim)

Trace run1 CLOSED. İstanbul saatleriyle25.10 03:52:05 ilk/tek canlı başarılı
okuma;05:51:27 son obs_page pasif örneği;05:52:28 ilk login_screen;
08:00:06 AUTH_REQUIRED doğrulaması. Girişten giriş ekranına yaklaşık2saat
(2sa00dk24sn), fakat bu sunucu tarafında2saat geçerlilik kanıtı değildir:
ara canlı başarı yok, eski DOM sunucu oturumunu kanıtlamaz.08'deki4sa08dk
kapanış tespit gecikmesini içerir, oturum ömrü diye sunulmaz.
247 yerel örneğin tümünde bot/browser/VNC süreç kimlikleri aynı; trace olaylarında
restart/gap/clock change yok. systemctl güncel PID/start doğrulaması da aynı:
bot1783459, browser1473049, VNC1472624. Browser eski NRestarts1 bu deneyden
önce24.10 06:08'de oluşmuş. Dolayısıyla VNC/tarayıcı yeniden başlaması bu
deneyde desteklenmiyor; OBS yaklaşık2saatlik süre/aşım davranışı olası,
idle mi sabit ömür mü/başka giriş mi tek deneyle ayrışmaz. Şu an auth
AUTH_REQUIRED, login_pending yes. Kod/arm/servis/OBS sayfası değiştirilmedi.

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
bir kere bildirilmesini istedi. Gösterilen duyuru canlı DOM'
