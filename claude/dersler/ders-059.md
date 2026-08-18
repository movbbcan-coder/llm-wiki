---
ureten: hafiza-yayinla
tip: ders
no: 59
etiketler: [ders, rulebook]
---

# Ders 59 — Ekstre fotoğrafının cutoff'u "son işlem saati" DEĞİL "belgenin indirilme saati"dir — aradaki fark bildirim gecikmesi kadar bile olsa para İKİ KEZ düşer.

**Ekstre fotoğrafının cutoff'u "son işlem saati" DEĞİL "belgenin indirilme saati"dir — aradaki fark bildirim gecikmesi kadar bile olsa para İKİ KEZ düşer.** İş ekstresi 20:50:16'da indirildi ve 20:01:51'deki 15.000 ₺ çıkışını İÇERİYORDU (bakiye 300,52). Ama `beklenen_bakiye` cutoff'u `bakiye_ts or son` sırasıyla seçiyordu; bakiye_ts boş olunca `son` = ekstredeki SON İŞLEM saati (20:01:51) kullanıldı. Defterdeki virman kaydının damgası ise BİLDİRİMDEN geliyordu (20:02:31 — bankanın push'u işlemden ~40 sn sonra düşer) → 20:02 > 20:01:51 olduğu için "fotoğraftan sonraki hareket" sanıldı ve ekstrede zaten düşülmüş 15.000 bir kez daha düşüldü: **300,52 − 15.000 = −14.699,48** (kullanıcı: "finance eksi 14699"). P2P ekranı doğruydu çünkü o `ekstre_belge_damgalari` ile belge tarihini kullanıyordu (#49) — yani aynı kavramın iki yolundan biri düzeltilmiş, öteki unutulmuştu (#45 ailesi). Fix: cutoff sırası **bakiye_ts → belge_ts → son**; `son` yalnız belge damgası parse edilemeyen kaynaklar için son çare. Kural: bir damgayı cutoff yapmadan önce "bu damga fotoğrafın çekildiği an mı, içindeki son olayın anı mı?" diye sor (#28/#40'ın üçüncü tekrarı) ve **bildirim damgasının işlem damgasından saniyeler sonra olduğunu unutma** — eşitlik değil sıralama kırılır.

---
*Kaynak: İş Bankası Finans −14.699 ₺ 2026-08-01 → beklenen_bakiye cutoff sırası + test_ekstre_zaman_ekseni +4*
