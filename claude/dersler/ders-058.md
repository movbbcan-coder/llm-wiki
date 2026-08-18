---
ureten: hafiza-yayinla
tip: ders
no: 58
etiketler: [ders, rulebook]
---

# Ders 58 — Bir transferin iki ucu vardır; biri tutarı söylüyorsa KÖR olan ucun tutarı da odur — ama havuz ile ekran farklı davranmalı.

**Bir transferin iki ucu vardır; biri tutarı söylüyorsa KÖR olan ucun tutarı da odur — ama havuz ile ekran farklı davranmalı.** İş→Garanti 15.000 ₺ virmanında Garanti bildirimi tutarı söyledi ("BA**** MO**** tarafından 15.000,00 TL FAST"), İşCep söylemedi ("Hesabınızdan para gönderildi", #34 kör banka). Kimse iki bildirimi birleştirmediği için İş havuzu 15.700'de kaldı, ekran 15.883 ₺ gösterdi, para ise Garanti üzerinden Midas'a gitmişti; ayrıca Midas çıkışı Garanti'den düşülürken havuzda 363,63 ₺ olduğu için kalan 33.636 ₺ sessizce buharlaştı. Fix: `trading/virman.py` — gelen bildirimin göndereni HESAP SAHİBİ mi (maskeli ad eşleşmesi) + aynı pencerede BAŞKA bankadan kör çıkış sinyali var mı; İKİ kanıt birden yoksa virman kurulmaz (yanlış bankadan düşmek, hiç düşmemekten kötü — #29 ailesi). **Asıl incelik: havuz İKİ taraflı işlenir (para gerçekten yer değiştirdi) ama bakiye zincirine YALNIZ KÖR TARAF yazılır** — tutarı söyleyen tarafın bildirimi zincire kendi yolundan zaten biniyor, ikisini de yazmak aynı 15.000'i iki kez saymaktır. `DEFTER_YONU`'ya tip eklerken sorulacak soru: "bu hareketin ekrana binen BAŞKA yolu var mı?" (komisyon'da var → eklenmez; virman kör tarafında yok → eklenir); mevcut koruma testi bunu yakaladı. TUZAK: ham.jsonl UTC ('17:02:31Z'), sinyal.jsonl yerel ('20:02:57') damga yazıyor — ikisini aynı sanmak 3 saatlik kayma = eşleşme hiç kurulmaz.

---
*Kaynak: İş→Garanti 15.000 ₺ virmanı 2026-08-01 → trading/virman.py + beklenen_bakiye.DEFTER_YONU + hareket.TIPLER + test_virman.py (20 vaka)*
