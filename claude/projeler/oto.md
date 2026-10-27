---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

##2026-10-27 — Canlı profil ve öğrenci mail yolu audit (Codex; salt okunur)

Kullanıcı girişten sonra inceleme istedi. Canlı üst öğrenci menüsüyle öğrenci
numarası doğrulandı; önceki tahmini numara yanlıştı (kişisel değer burada tutulmaz).
Kayıtsız form değişikliği kontrolü false. Ders kayıt kapanış bilgilendirmesi
Tamam ile kapatılıp Profil normal menüsünden ogr_ozluk.aspx açıldı; yalnız
e-posta etiketli alanlar okundu. İki kişisel e-posta var, kurumsal öğrenci
adresini gösteren alan yok. Hiçbir değer değiştirilmedi veya form gönderilmedi.
Kurumsal adres formatı hesap etkinliği kanıtı değildir. Resmî/e-posta sayfası
E-Posta Öğrenci bağlantısını Google/accounts.google.com'a, personel bağlantısını
Outlook'a veriyor; kullanıcıya doğru öğrenci yolu sunulacak. Login/şifre işlemi yok.
Canlı menü envanteri: danışman/devamsızlık, gelen-gönderilen mesajlar, yapılacaklar,
belge talebi, tez/seminer/mazeret/kayıt dondurma başvuruları bulunuyor; içerikleri
bu tur doğrulanmadı. Dosya/materyal listesi ana menüde görülmedi; Pusula ayrı
kaynak olabilir, henüz entegrasyon yok. Öğrenci numarası/eposta/oturumlu route
parametreleri kalıcı audit'e kopyalanmadı. E2 run3 ACTIVE; son canlı başarı
27.10 23:39:50 İstanbul; aradaki donma/yeniden kullanıcı girişi nedeniyle run
yaşını kesintisiz tek oturum ömrü sayma. Browser/VNC restartı yok.

##2026-10-27 — VNC tıklamama kök nedeni: MemoryHigh baskısı (Codex; toparlandı)

Yeni görseller sonrası host ölçümü: Chrome1473049 Dsl,
wchan=mem_cgroup_handle_over_hi; cgroup MemoryCurrent581091328,
MemoryHigh536870912,MemoryMax805306368. memory.events high114719345,
oom/oom_kill0; PSI full avg10=98.20.9233 LISTEN RecvQ7 ve HTTP000.
Host MemAvailable3020804096. Yalnız runtime systemctl set-property ile
MemoryHigh768M/MemoryMax1G uygulandı (eski512M/768M); swap128M aynı,
servis restartı yok. Ardından HTTP200, aynı1473049 Ssl/do_poll; PSI düşüyor.
Bu olayın yerel takılma nedeni bellek baskısıdır, OBS TTL olarak yorumlanamaz.
CDP'de yalnız chromewebdata hata sekmesi kaldığı görüldü; kullanıcı sayfa
onarımı kapsamında aynı hata sekmesi resmî OBS login.aspx'e açıldı:
HTTP200,/oibs/std/login.aspx, password alanı sayısı2 (değer okunmadı).
Bot/VNC/tarayıcı restartı, login veya Telegram mesajı yok. Kişisel mail/numara
henüz doğrulanmadı. Runtime sınır reboot sonrası kalıcı değildir; deploy unit
hâlâ512M/768M. Sonraki iş: sınır kaynaklarını/testleri tutarlı kalıcı ayara
taşımak, PSI/MemoryHigh olaylarını oturum deneyinden ayrı izlemek. Geri dönüş
runtime MemoryHigh512M/MemoryMax768M; donmayı geri getirebileceği için ölçmeden
uygulama. Önceki oturum kapanışlarının tümünü bu vakaya bağlayacak kanıt yok.

##2026-10-27 — VNC OBS yükleme takılması (Codex; normal yenileme denendi)

Kullanıcı yükleme ekranında sayfayı yenileyemediğini bildirdi. CDP9233
host erişimi5sn Timeout; curl6sn HTTP000. Browser1473049 active/running,
151task,581MB,MemoryPeak582MB; son dar journal kesitinde olay yok. Bunlar
OOM veya OBS oturum kapanış kanıtı değildir. VNC mount namespace üzerinden
odak pencere OBS index.aspx olarak doğrulandı; kullanıcı isteğiyle yalnız
Ctrl+R gönderildi. Sonrasında CDP hâlâ HTTP000, odak aynı. Sayfanın toparlandığı
doğrulanamadı. Browser/VNC/bot restartı ve giriş yapılmadı, credential okunmadı.
Sonraki güvenli adım yalnız OBS browser yeniden başlatma için kullanıcı onayı;
yeniden giriş gerekebilir. Mail adresi/öğrenci numarası henüz canlı doğrulanmadı.

##2026-10-26 — E2 onaylı canlı geçiş (Codex; WAITING)

Kullanıcı açık onayıyla E2 üç ürün dosyası aynı bota aktarıldı. Önkontrol
PREFLIGHT_OK; canlı hashler RELEASE ile aynı. Yedek kod+SQLite:
`veri/universite/releases/session-e2-20261026T105828Z`; uygulama ve metadata
geri dönüş aracı `.work-beykent-e2/deploy/apply_e2.py`. E2/900sn hazır,
arm26.10 13:58:28 İstanbul; worker heartbeat13:58:29 ve bot kimliği doğrulandı.
Bot2544202 active/NRestarts0. Browser1473049 ve VNC1472624 PID/start
kimlikleri değişmedi; test mesajı0. Önceki iki CLOSED run korundu; WAITING
yeni canlı giriş doğrulaması bekliyor. İlk15dk denemesi ve süreklilik henüz
ölçülmedi. Önceden izole556 test geçti; bu tur yeniden ürün değişikliği yok.
Kullanıcı VNC girişi + Telegram Girişi tamamladım/doğrula düğmesine yönlendirilecek.

##2026-10-26 — E2 hazırlığı tamamlandı (Codex; canlı geçiş bekliyor)

Kullanıcının hazırlık/status isteğiyle gerçek geliştirme bu turda yapıldı.
İzole `.work-beykent-e2`: E1 korunarak E2/900sn ayrı kalıcı metric/deneme
işareti; kapanmış run sonrası yalnız yeni canlı doğrulanmış başarıyla ayrı run;
eski kayıtlar korunur. Yanıltıcı 'açık süre' metni doğrulamalar arası süre olarak
düzeltildi. Reader ham hata/sır yerine izinli sabit hata sınıfları kaydeder.
Üç dosya için etki kapısı çalıştı; yeni10 test + eski546 =556/556 geçti23,09sn,
6 eski uyarı,ağ kapalı/root salt okunur. RED ilk import eksiği; GREEN tam suite.
Canlı kod/metadata/servis değişmedi, üretim onayı bekleniyor. Diff/hash ve
deploy/apply_e2.py salt okunur PREFLIGHT_OK. Özel yedek+rollback ve aktif run
koruma mevcut; browser/VNC değişmez. Tam inceleme `.work-beykent-e2/docs/E2_RELEASE.md`.
Önceki navigation hatasının sebebi hâlâ kesin değil; yeni sınıflandırma yalnız
gelecek olayı ayrıştırır. Kullanıcı girişini yeni sürüm hazır olmadan isteme.

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
kopyası7 hata verdi; deploy dosyal
