---
ureten: hafiza-yayinla
tip: ders
no: 41
etiketler: [ders, rulebook]
---

# Ders 41 — Test araçları (mutmut/diff-cover/jscpd/testmon) YANLIŞ ÖNCÜLÜ yakalayamaz — mutabakat testi yakalar.

**Test araçları (mutmut/diff-cover/jscpd/testmon) YANLIŞ ÖNCÜLÜ yakalayamaz — mutabakat testi yakalar.** 2026-07-21 regresyonunda değişen satırların hepsi testliydi, süit 1100 yeşildi, mutantlar ölüyordu — ve gerçek para ekrandan silinmişti. Sebep: testler kodun öncülünü doğruluyordu, öncülün kendisi yanlıştı; jscpd de kaçırdı çünkü 4 katmandaki kopya **kavramsaldı, metinsel değil**. Yakalayabilecek tek şey **ekran ↔ bağımsız dış kanıt mutabakatı** (`defter/teshis.py`) idi ama o yalnız `beklenen_bakiye` zincirine bakıyordu; kullanıcının baktığı `/data.json` yolunu HİÇ denetlemiyordu (#35'in tekrarı: denetlenmeyen yol denetlenmiş sanılır). **Kural: aynı olguyu gösteren HER ekran yolu mutabakata dahil olmalı; "testler yeşil" bir ekranın doğru olduğunun kanıtı DEĞİLDİR.** Ayrıca invaryant testi yaz: sayıyı değil sıralamayı kilitle (`belge_ts > midas_cutoff`).

---
*Kaynak: araç yeterliliği sorgusu 2026-07-21 → test_ekstre_zaman_ekseni.py sıralama kilidi*
