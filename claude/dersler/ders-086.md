---
ureten: hafiza-yayinla
tip: ders
no: 86
etiketler: [ders, rulebook]
---

# Ders 86 — Bir bayrağı açmak YETENEĞİ açmaz — "açık" diyen ekran ile "yapabilir" olan sistem ayrı şeylerdir; ikisi senkron değilse kullanıcı sessiz başarısızlıkla baş başa kalır.

**Bir bayrağı açmak YETENEĞİ açmaz — "açık" diyen ekran ile "yapabilir" olan sistem ayrı şeylerdir; ikisi senkron değilse kullanıcı sessiz başarısızlıkla baş başa kalır.** Bankalar günlük işlem limitini doldurunca BW ilanı çekti ama `tl_aktif` bayrağı True kaldı: Telegram "TR pazar AÇIK" diyor, piyasada ilan yok. Kullanıcı özel bir müşteri için elle ilan açmak istedi, tuşa bastı, **"açıldı 🟢"** cevabını aldı ve hiçbir şey olmadı — çünkü bayrak zaten açıktı, engel bankaydı ve kimse sebebi söylemiyordu. Üstelik log'daki sebep de YANLIŞTI: "tüm TRY bankaları dolu" diyordu, gerçek tablo ise *2 banka kota doldurmuş · 1 banka hesabı bankaca kapatılmış · 1 bankanın Bybit'te ödeme yöntemi hiç tanımlı değil*. Kullanıcı bu mesaja inanıp Enpara'nın kullanılabilir olduğunu sandı. **Yanlış sebep, sebepsizlikten kötüdür.** Fix: `banka_risk.kapasite_teshis` (banka başına gerçek sebep) + `pazar.kapasite_senkron` (kapasite bitince pazar oto-kapanır ve Telegram'a sebebiyle bildirilir; kapasite dönünce oto-açılır) + elle açmada kapasite yoksa sebebi söyleyen uyarı. YAN BULGU 1 — **`kaydet_state()` sabit anahtar listesi yazıyor**: eklediğim `tl_oto_kapandi` diske hiç düşmedi, restart'ta kaybolup pazar sonsuza dek kapalı kalacaktı (#30'un state şeması hâli: yeni alan eklersen kaydet/yükle şemasına DA ekle; canlı ölçüm olmadan görünmezdi). YAN BULGU 2 — **koşulu işaretin VARLIĞINA bağlamak kırılgandır**: "oto-kapattım işareti varsa aç" yerine "kullanıcı elle kapatmadıysa aç" kuruldu; işaret bir şekilde kaybolsa bile güvenli taraf (açmak = para kazanmak) korunur, kullanıcı kararı ise ayrı izle (`tl_elle_kapandi`) saklanır (#42'nin dayanıklı biçimi). YAN BULGU 3 — kapasite kontrolü ilan İPTALİNDEN SONRA yapılıyordu: uygun banka olmadığı sürece BW her 30 saniyede 10 kapalı ilanı boşuna iptal ediyordu (canlı logda ölçüldü); kontrol öne alındı.

---
*Kaynak: TL pazar ↔ banka kapasitesi senkronu 2026-08-17 → banka_risk.kapasite_teshis/kapasite_sebep_metni + pazar.kapasite_senkron + tr_ac(elle) + p2p_state şeması + dongu_bakiye ön-kontrol + test_pazar_kapasite.py (24)*
