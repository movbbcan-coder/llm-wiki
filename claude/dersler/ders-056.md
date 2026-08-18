---
ureten: hafiza-yayinla
tip: ders
no: 56
etiketler: [ders, rulebook]
---

# Ders 56 — Sınıfı ADINA göre değil, KULLANICIDAN NE İSTEDİĞİNE göre ayır — "izin" ile "sana soru sordum" aynı ihtiyaçtır.

**Sınıfı ADINA göre değil, KULLANICIDAN NE İSTEDİĞİNE göre ayır — "izin" ile "sana soru sordum" aynı ihtiyaçtır.** Termux çağrı sisteminde bildirimler IZIN / BEKLER / HAZIR diye ayrıldı; BEKLER "60 sn boşta" sanılıp telefonu+oturumu çekmekten muaf tutuldu. Ama Claude'un SORU SORDUĞU hâl (AskUserQuestion) da o sınıfa düşüyor: kullanıcı Instagram'dayken Termux'a atıldı, cc-denk ekranda kaldı, soru cc-ceo'daydı — soruyu bulamadı, "anlamadım" dedi. İkisi de aynı şeyi ister: kullanıcının gelip cevap vermesi. Fix: kapı `SINIF=IZIN` yerine `SINIF!=HAZIR`. **Kural: bir dalı dışlarken "bu sınıfa gerçekte hangi olaylar düşüyor?" diye sor — ad ("bekler") olayların tamamını anlatmıyor olabilir** (#48/#42 ailesi: bayrağın gerçek anlamı). İKİNCİ DERS: ortam değişkeni kimlik kaynağı DEĞİLDİR — `$TMUX` fork edilmiş oturumda boştu, etiket `[test]`e düşüyor ve geçiş sessizce hiç tetiklenmiyordu; `tmux display-message` yedeği de yanlış cevap verir ("en son bağlanılan" oturumu döndürür, çağıranı değil). Doğrusu: kendi süreç ata zincirini pane PID'leriyle eşleştir — kimliği tahmin etme, TÜRET. ÜÇÜNCÜ DERS: **tekrar-bastırma kapısını METNE dayandırma.** Tek izin isteği, metni birbirinden az farklı İKİ bildirim üretti (06:53:00 + 06:53:04); imza=başlık+mesaj olduğu için ikisi de geçti. Zarar gürültü değildi: ikinci çağrı geldiğinde Termux ARTIK ön plandaydı, telefon tarafı "önceki uygulama"yı Instagram yerine **Termux** diye kaydetti → geri dönüş "Termux'u başlat"a dönüştü, yani sessizce kendini iptal etti. Kapı SINIF+SÜRE olmalı (25 sn), metin değil. DÖRDÜNCÜ: teşhis için iz şart — üç tur "çalıştı mı?" diye tahmin yürüttük, `/tmp/claude-cagri.log` eklenince tek bakışta görüldü (ve ironi: ilk kanıtı kendi temizlik komutum sildi — log'u sildiğin komut, ölçmek istediğin olayı da siler).

---
*Kaynak: Termux çağrı sistemi 2026-07-29 → termux_push.sh _oturum_bul + sınıf/süre kapısı + geri-don.sh + TERMUX_CAGRI.md*
