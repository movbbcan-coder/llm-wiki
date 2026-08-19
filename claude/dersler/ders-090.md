---
ureten: hafiza-yayinla
tip: ders
no: 90
etiketler: [ders, rulebook]
---

# Ders 90 — Bir nöbetçi, ÇARESİ OLMAYAN arızaya müdahale etmeye devam ederse hem boşuna çalışır hem onarımı ENGELLER.

**Bir nöbetçi, ÇARESİ OLMAYAN arızaya müdahale etmeye devam ederse hem boşuna çalışır hem onarımı ENGELLER.** Bybit lamba nöbetçisi 15 saatte **497 kez** müdahale etti ve hiçbiri işe yaramadı: arıza "sekme çöktü" değil **"web oturumu düştü"** idi (kanıt: sanal ekranın görüntüsünde sağ üstte `Log In / Sign Up`). Nöbetçi şifre giremez — bu sınır tasarımda YAZILIYDI ama koda GİRMEMİŞTİ, o yüzden her 5 dk'da `basla.sh` ile Chrome'u SIGKILL edip yeniden kuruyordu; kullanıcı tam o sırada noVNC'den giriş yapsa girişi de ölecekti (#64 ailesi: yardım eden şey yardım ettiği işi deviriyor). Üstüne susma sabit 3600 sn olduğu için kullanıcı 15 saat boyunca aynı mesajı aldı ve "çok bildirim geliyor" dedi — yani koruma kendi kanalını çöpe çeviriyordu (#82 birebir tekrar). Fix: (a) N denemede etki ölçülmüyorsa hâl `GİRİŞ GEREKLİ`ye geçer ve **müdahale DURUR** (tarayıcıya dokunulmaz), (b) haber aralığı merdiveni 30dk→2sa→8sa→24sa, ışık yanınca sıfırlanır, (c) noVNC'de ESTABLISHED bağlantı varsa (insan ekranda) hiçbir müdahale/haber yok — ölçülür, tahmin edilmez, (d) susturma dosyası (`.sessiz`) haberi keser ama izlemeyi sürdürür, (e) "hiç haber verilmedi" sentinel'i `None` (#80). Kural: **her otomatik onarıcı "benim düzeltemeyeceğim hâl" sınıfını AÇIKÇA taşımalı; o hâlde doğru davranış müdahaleyi bırakıp insana yer açmaktır.** YAN BULGU: yığının PM2 servisi (`bybit-lamba`) STOPPED'dı, tarayıcıyı nöbetçi ayakta tutuyordu — bekçisi durmuş bir sistemi başka bir bekçi taşıyorsa arıza görünmez olur.

---
*Kaynak: Bybit lamba oturum düşmesi 2026-08-19 → bybit_lamba/karar.py (saf çekirdek) + nobetci.py + tests/test_karar.py (10, 3 kapı mutasyonla doğrulandı)*
