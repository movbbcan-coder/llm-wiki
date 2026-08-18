---
ureten: hafiza-yayinla
tip: ders
no: 37
etiketler: [ders, rulebook]
---

# Ders 37 — Kaza nöbetçisine BİRİKİMLİ olmayan alan koyma — #32'nin İKİNCİ kurbanı: transit kuyruğu.

**Kaza nöbetçisine BİRİKİMLİ olmayan alan koyma — #32'nin İKİNCİ kurbanı: transit kuyruğu.** `midas_bekleyen` `_KORUNAN`'daydı; ama o boşalan bir TRANSİT kuyruğu (tüm lotlar Bybit'e gelince meşru 0). Son lotlar gelince liste 3→0/1 düşünce KAZA NÖBETÇİSİ "disk 3 / bellek 0 → yüklenmemiş state" sanıp yazımı REDDETTİ → `midas_kombine_kayit`'in transit silmesi diske yazılamadı → transit diskte kaldı → restart'ta geri geldi → **Bybit + transit ÇİFT SAYIM (kullanıcı "hesap şişti")**. Guard bir felaketi (kural #31 unloaded-wipe) önlerken başkasını (çift sayım) üretti — #32 ile birebir sınıf (gunluk_satis). **Kural: guard yalnız GERÇEKTEN birikimli, meşru boşalmayan alanı korur (alim_kayitlari, maliyet_havuzu, islenen_siparis_ids). Unloaded-wipe felaketi zaten islenen_siparis_ids (hep 60+) çöküşünden yakalanır; orijinal kazada guard'ı kurtaran da oydu, midas_bekleyen 2 lot eşiğin altındaydı hiç tetiklemedi.** TUZAK 2: transport (bybit_client) GET imzasını `sorted(params)` üretir ama insertion-order gönderir → çok-parametreli GET'te params ALFABETİK verilmeli, yoksa "Error sign".

---
*Kaynak: Midas→Bybit transit şişmesi 2026-07-18 → p2p_state._KORUNAN (midas_bekleyen çıkarıldı) + test_state_kaza_nobetcisi.py +3 + bybit_isler.bybit_deposit_gecmisi*
