---
ureten: hafiza-yayinla
tip: ders
no: 35
etiketler: [ders, rulebook]
---

# Ders 35 — "Denetleyemiyorum" da bir bulgudur — susan koruyucu, olmayandan BETERDİR (var sanılır).

**"Denetleyemiyorum" da bir bulgudur — susan koruyucu, olmayandan BETERDİR (var sanılır).** Nöbetçinin K1-K9 öncülleri tarandı (Fable denetimi + canlı ölçüm); üç sessiz-körlük bulundu: (a) `gb.ok=False` → hayalet denetimi else dalı olmadığı için sessizce kapanıyordu (havuz 99.999 vs gerçek 1 → SIFIR bulgu); (b) `if satislar and tl_aktif` → defter TAMAMEN ölünce "defter canlı mı?" kontrolü susuyordu (**#32'nin birebir sınıfı: izlenen arıza izleyicinin girdisini öldürüyor**); (c) dış kanıtta karşılığı olmayan banka kör kümesine giremediği için "görünür" sayılıp sahte KRİTİK üretiyordu — **en kör banka en çok hüküm giyiyordu**. Kural: her koruyucuda "denetleyemediğim hâl" AYRI bir bulgu üretmeli; ayrıca aynı olguya bakan iki kontrol (K3/K4) AYNI politikayı izlemeli — biri atlayıp diğeri bağırıyorsa biri yanlış. Bonus ders: ajan iddiasını ölçmeden kabul etme — 4 iddianın 1'i yanlıştı (`kor` saklanmıyor, her turda yeniden hesaplanıyor)

---
*Kaynak: nöbetçi öncül denetimi 2026-07-16 → nobetci K3 else + K7 boş-defter + K9 kanıtsız + test_nobetci_oncul.py*
