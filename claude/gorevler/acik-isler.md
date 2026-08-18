---
ureten: hafiza-yayinla
tip: gorev
etiketler: [acik-is]
---

# YARIM KALANLAR — Faz Kütüğü (zincirin ilk halkası)

> **FOCUS emekli oldu (2026-07-25).** Tek-çıpa disiplini tutmadı. Yeni yöntem:
> Claude analiz eder; bir faz bitmeden başka projeye geçilirse yarım kalan BURAYA yazılır;
> **her tamamlanan işten sonra Claude buradaki yarımları bitirmeyi proaktif önerir.**
> Öncelik: önce öncelikli/aktif projeler → sonra yarımlar yavaş yavaş kapanır.
> Zincirin ilk halkası koparsa buradan bulunur (hafıza kritik → [[feedback-yarim-kalanlar]]).

## Kural (Claude'un davranışı)
1. **Faz ortası geçiş = kayıt.** Bir projenin fazı bitmeden başka işe geçiyorsak, çıkmadan
   önce bu tabloya satır ekle: nerede kaldı + neden bırakıldı + devam koşulu.
2. **Her iş bitiminde hatırlat.** Bir görev/faz tamamlanınca, bu tablodan uygun bir yarımı
   "şimdi buna dönelim mi?" diye ÖNER (dayatma değil — kullanıcı önceliği bilir).
3. **Devam koşulu tetiklenince öne çıkar.** Bir yarımın "devam koşulu" gerçekleştiyse
   (ör. pazar açıldı, ekstre geldi) onu üste taşı ve özellikle hatırlat.
4. **Biten satırı arşive taşı** (aşağıdaki "Kapananlar"), silme — iz kalsın.

## AÇIK YARIMLAR (öncelik sırası)
| # | Proje | Faz / İş | Nerede kaldı | Neden bırakıldı | Devam koşulu | Öncelik |
|---|-------|----------|--------------|-----------------|--------------|---------|
| Y1 | **VPS Hijyen** | Tur-1 bitti (~460M silindi + memory MCP kaldırıldı). Kalan: logs 62M arşiv, skill/kural hijyeni, link_bio kararı | Tur-1 tamam | Proje proje devam | 🔴 aktif |
| Y2 | **P2P DEFTER** | DEFTER FAZ 3 (okumaları deftere çevir) | FAZ 2 gölge; pencere 22.07'de doldu | Öncelik başka yerdeydi | Gölge sapması 0 teyit → FAZ 3 | 🟡 orta |
| Y3 | **lise_diplomasi → ticari** | Çalışmayı para kazandıran ürüne dönüştür | Veri/çalışma var, verim alınmadı | Kullanıcı "boşa gitmesin, geliştir" dedi | Ticari fikir netleşince | 🟡 orta |
| Y6 | **Denk → Play yayını** | Kod ve mağaza malzemesi HAZIR; kritik yol takvimde | 265 test yeşil, release imzalı, görsel+metin hazır (/root/denk/magaza/) | Play KİŞİSEL hesabı ($25) kullanıcıda; D-U-N-S GEREKMİYOR (ADR-002) | Hesap açılınca: 12 tester × 14 kesintisiz gün → 7 gün inceleme (~3 hafta) | 🔴 aktif |
| Y4 | **obsidian → Claude hafızası** | Vault'u (55 md) telefona bağla + üst-seviye Claude CLI hafızası planı | Vault duruyor, karar bekliyor | Değer analizi gerek | Verimli olacaksa plan yap, değilse sil | ⚪ düşük |
| Y5 | **P2P Kuzen kaldırma** | PM2 (kuzen-bot/idle) durduruldu + kod DEPO'da; AMA p2p'ye 107 ref (callback, ekstre_harcama=para) → kod sökümü = refactor | Standalone servis durdu; kod entegre | Ayrı careful refactor (KAPI+test) | ⚪ düşük — körlemesine silme |

## KAPANANLAR (iz)
| Tarih | Proje | İş | Sonuç |
|-------|-------|-----|-------|
| 2026-07-25 | Çalışma metodu | 5-konu araştırma + İş Defteri + Hafıza SSOT + CODEMAP + KAPI characterization + denetim | ✅ RAPOR.md, skor 7.8→8.3 |
| 2026-07-25 | Hijyen tur-1 | Sildi: jcode_bench(138M)·tradingview-mcp(273M)·instagram_bot(28M)·kastaliya_menu(15M)·jcode_bench2·veles_x.bak·2 switch-backup·__pycache__·kapi_selftest·concierge·pubgrent·emergent + memory MCP | ✅ ~460M · KURTULDU (canlı çıktı): ai_dashboard(PM2 3004)·router(model_router)·link_bio(nginx /files)·tm_vpn(kaynak) |
| 2026-07-25 | P2P bug | Midas kaynak-banka tuşu: Garanti (satışa kapalı) düşmüştü → aktif filtresi kaldırıldı, saf fn + test, 6.800 bildirimi Garanti tuşuyla yeniden atıldı | ✅ 1182 test yeşil |
| 2026-07-26 | P2P Is fis cutoff | Bildirimsiz banka fis cutoff ekstre belge tarihi (07-21) kullanir oldu, defter-satis ts degil; ekstre_belge_damgalari helper + test | OK Is 183->45 Finance ile birebir, 1184 test, restart gerekmedi |
| 2026-07-27 | Hijyen tur-2 (skill) | gstack web'e indirildi: 37 skill arsive (iOS 5 + dev-workflow); 55->24 dizin; ozel+web+altyapi kaldi | OK geri-alinabilir arsiv |
| 2026-07-27 | Friction-avi (lean-ctx) | lean-ctx v6 native-deny + Turkce char-boundary cokme cozuldu: deny temizlendi, 9 hook + MCP kaldirildi, CLAUDE.md native-birincil, shell-hook off | OK native araclar temiz calisiyor, KAPI/session hooklari korundu |
| 2026-07-27 | Friction-avi tur-2 | rm-guard sinir-farkindali (danger_check.py+23 test), stale glm/zai_shell/ctx_shell delegasyon refleri native yapildi, olu MCP kayitlari (lean-ctx global+zai) silindi, MCP tablosu gercege cekildi, lean-ctx skill arsive | OK 6 friction giderildi |

## Telefon: ntfy + MacroDroid doğrulaması (ccvps oturumunda)
*2026-07-29 · nerede kaldı: VPS tarafı HAZIR, telefon tarafı doğrulanmadı*

VPS'te kurulu: `/root/.claude/hooks/izin-bildirim.sh` → ntfy konusu `claude-izin-fab894279a`.
Telefonda kontrol edilecek:
1. **ntfy** uygulaması kurulu mu, `claude-izin-fab894279a` konusuna abone mi?
2. MacroDroid makrosu var mı: Bildirim Alındı (uygulama: ntfy, metin içerir `CLAUDE IZIN`)
   → Uygulama Başlat: Termux
3. DİKKAT: makro yalnız `CLAUDE IZIN` için kurulacak. Hook ayrıca `CLAUDE BEKLER`
   (60 sn boşta) gönderiyor; ona da bağlanırsa her duraklamada telefon elden gider.
4. Termux'ta mosh kurulumu: `pkg install -y mosh openssh` + ~/.bashrc kısayolları
   (belge: `/root/TERMUX_KURULUM.md`)

**Devam koşulu:** `ccvps` oturumunda yapılacak — Denk/APK oturumuyla karıştırma.

## Termux çağrı — "izin verince otomatik geri dön" (2026-07-29) ✅ KAPANDI
CANLI ve doğrulandı: gerçek izin isteğinde Termux'a çekti, onaydan ~4 sn sonra
kullanıcıyı Instagram'a geri döndürdü. Zincir: termux_push.sh (bayrak) →
PostToolUse/geri-don.sh → MacroDroid `Claudegeri` webhook → Uygulama Çalıştır {v=onceki}.
Telefon tarafı: `Claude → Termux` makrosu önce `onceki={fg_app_package}` (Dize, Genel)
kaydeder, sonra Termux'u açar. Belge: /root/.claude/hooks/TERMUX_CAGRI.md

## ccoto oturumu — ccoto DIŞINDA kalan açık işler (2026-08-18)

Ana iş defteri: `/root/ccoto/LEDGER.md` (başında "YENİ OTURUM — BURADAN BAŞLA" bloğu var,
yeni oturum önce onu okusun). Aşağıdakiler o defterin KAPSAMI DIŞINDA ama açık:

### 1. 🔴 claude1 aboneliği — 15 Ağustos'ta bitiyordu, DURUMU BİLİNMİYOR
Ölçüm (2026-08-12): `movbbcan@gmail.com` → `subscription_status: canceled`,
`billing_type: google_play_subscription`, son çekim 15/07 (1.043,75 ₺). Google Play'de
iptal edilmiş abonelik dönem sonuna kadar çalışır → **15 Ağustos'ta kesilmiş olabilir.**
Kullanıcı "yarın ben bakarım" dedi (13 Ağustos), sonucu konuşulmadı.
Kontrol: `bash /root/.claude/usage-fetch.sh` + `/api/oauth/profile` (usage-fetch.sh içinde
güvenli refresh deseni var; rulebook #26 — refresh token ROTATE eder, dikkat).

### 2. 🟠 claude2 aboneliği — ödeme başarısız (past_due)
`movbbcan23@gmail.com` → `subscription_status: past_due`, `billing_type: stripe_subscription`.
Yenileme günü ayın **12'si**, kart: **Enpara Encard, son 4 hane 2700**. Kesilme sebebi kota
DEĞİL, ödeme. (claude1 → Google Play üzerinden, yenileme ayın **15'i**, aynı kart.)
Çözüm: karta bakiye + claude.ai/settings/billing'den ödemeyi tekrar dene.

### 3. 🟠 Bash izin sistemi bu VPS'te KAPALI — kullanıcı kararı bekliyor
Ölçüldü (2026-08-12): `settings.json` → `PreToolUse matcher=Bash|bash` →
`lean-ctx hook rewrite` **her Bash komutuna koşulsuz `{"permissionDecision":"allow"}`**
dönüyor. 571 satırlık allowlist fiilen anlamsız; hangi komut gelirse gelsin sorulmuyor.
Tehlike guard'ı (`pre-tool-use.sh`) sağlam — `deny`, `allow`'u yener.
Bu, rulebook #50 temizliğinin yarım kalan parçası (MCP + shell hook gitti, PreToolUse kaldı).
Karar: hook'ları yedekleyip kaldırmak mı, böyle bırakmak mı? Kullanıcıya soruldu, cevap yok.

### 4. 🟢 Kapanan: Termux scroll sorunu
Parmakla kaydırma alt-ekranda ok tuşuna çevriliyordu (prompt geçmişi geliyordu).
Çözüm: `~/.termux/termux.properties` → extra-keys'e PGUP/PGDN. Ders: rulebook #78.

## 🔴 Obsidian kasası — GitHub jetonu geçersiz (2026-08-18)
Kasa (`/root/obsidian/vault` → `movbbcan-coder/llm-wiki`) **5 Haziran'dan beri** itilmiyordu;
sebep: `.git/config` remote URL'indeki jeton artık kabul edilmiyor ("could not read Password").
Ayrıca o jeton AÇIK METİNDİ — her `git remote -v` çıktısında sızıyordu; **iptal edilmeli**.

Yapıldı: remote URL temizlendi (jeton yok), `credential.helper store --file=/root/.git-kimlik`
(chmod 600) kuruldu, `hafiza-yayinla` yazıcı + 4 saatte bir cron kuruldu. 530 commit itilmeyi
bekliyor.

**Kullanıcıdan gereken:** GitHub'da eski jetonu İPTAL et, yeni bir tane üret (repo yazma yetkisi),
sonra tek komut: `hafiza-token <yeni_token>` → jetonu güvenli dosyaya yazar ve push'u dener.
