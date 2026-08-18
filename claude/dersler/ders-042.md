---
ureten: hafiza-yayinla
tip: ders
no: 42
etiketler: [ders, rulebook]
---

# Ders 42 — Bir bayrak İKİ farklı sebeple set ediliyorsa (biri geçici biri kalıcı), reset yalnız geçici olanı geri almalı — yoksa ya kalıcı karar ezilir ya geçici kilit sonsuzlaşır.

**Bir bayrak İKİ farklı sebeple set ediliyorsa (biri geçici biri kalıcı), reset yalnız geçici olanı geri almalı — yoksa ya kalıcı karar ezilir ya geçici kilit sonsuzlaşır.** `banka_aktif` hem limit-dolunca (geçici, ertesi gün açılmalı) hem kullanıcı-manuel (kalıcı) False oluyordu. Gün devri (`banka_limit_sifirla`) `kullanilan`/`islem` sıfırlıyordu ama `aktif`'i açmıyordu → oto-kapanan banka sonsuza dek pasif (İş Bankası 07-18→07-23, 5 gün; Garanti dolunca ilan çekildi, sessizce). Reset'e "hepsini aç" koymak da yanlış olurdu: kullanıcının manuel kapattığı Enpara'yı ezerdi. Çözüm: `banka_oto_kapandi` işareti — reset yalnız İŞARETLİYİ açar. Kural: "kapat" ile "aç" simetrik olmalı ve reset sebebi ayırt etmeli; tek bayrağa iki anlam yüklersen biri sessizce kaybolur. (rulebook #32/#37'nin akrabası: guard/reset kapsamı, gözetlediği durumun SEBEBİYLE eşleşmeli.)

---
*Kaynak: İş Bankası oto-kapanma kilidi 2026-07-23 → banka_kota.banka_oto_kapandi + banka_limit_sifirla + test_banka_kota +3*
