---
ureten: hafiza-yayinla
tip: ders
no: 98
etiketler: [ders, rulebook]
---

# Ders 98 — Oturumunu profile yazan bir tarayıcı, 7/24 çalışırken sessizce sekme biriktirir — ve o birikme makineyi devirir.

**Oturumunu profile yazan bir tarayıcı, 7/24 çalışırken sessizce sekme biriktirir — ve o birikme makineyi devirir.** OOM'un (#97) asıl sebebi tek satırlık bir davranıştı: Chrome kapanırken açık sekmeleri profile yazar, açılışta hepsini geri yükler. Aylar içinde lamba sekmeleri birikmiş, ekranda sekme çubuğu tamamen dolmuş ve aktif sayfa bybit değil `google.com/chrome/` olmuştu (yani lamba görevini de yapmıyordu, kimse fark etmemişti — göstergenin kendisi denetlenmiyordu). Ölçüm: 13 süreç · cgroup 802/900 MB. Temizlik sonrası: **1 sekme · 10 süreç · 595 MB**. Fix iki katmanlı: (a) `basla.sh` her başlangıçta `Sessions`/`Current Tabs`/`Last Session` siler → tek sekme, hedef URL; (b) `Cookies` ASLA silinmez — giriş kaybolursa lamba kalıcı söner ve nöbetçi şifre giremez (#90), yani "temizlik" korumayı öldürürdü. Kural: **kalıcı profille çalışan uzun ömürlü bir tarayıcıda oturum geri yüklemesi kapatılır; silinen ile korunan açıkça ayrılır.** YAN DERS (tekrar eden kendi hatam): kapıyı bash testiyle kilitledim, iki mutasyon da YAKALANMADI — `grep` aranan metni **yorum satırlarında** buluyordu ("MemoryMax=900M → sert tavan" diye bir açıklama vardı). Kod satırı ile yorumu ayırmayan kaynak testi kapı değil dekordur; `grep -vE '^[[:space:]]*#'` ile süzülünce iki mutasyon da kırmızıya döndü. Aynı sınıf #96'da da çıkmıştı (import'u çağrı sanmak): **kaynak-metin kilidi yazarken "bu desen KOD'da mı, yoksa anlattığım yerde mi eşleşiyor?" diye sor.**

---
*Kaynak: Lamba sekme birikmesi 2026-08-25 → basla.sh oturum temizliği + bybit_lamba/tests/test_tek_sekme.sh*
