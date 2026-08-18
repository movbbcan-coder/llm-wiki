---
ureten: hafiza-yayinla
tip: ders
no: 48
etiketler: [ders, rulebook]
---

# Ders 48 — Bir bayrağı ait olmadığı bir kapıda filtre olarak kullanma — `aktif` "satış alır mı"yı yönetir, "para kaynağı olabilir mi"yi DEĞİL.

**Bir bayrağı ait olmadığı bir kapıda filtre olarak kullanma — `aktif` "satış alır mı"yı yönetir, "para kaynağı olabilir mi"yi DEĞİL.** Midas kaynak-banka tuşları `BANKS` filtresinde `info.get("aktif")` kullanıyordu → Garanti satışa kapatılınca (aktif=False, #42) kaynak tuşu KAYBOLDU; kullanıcı Garanti'den Midas'a attı ama tuş yoktu (para düşülemez). Satışa kapalı banka birikmiş TL'yi hâlâ gönderebilir. Fix: filtreyi saf `midas_kaynak_banka_adlari(BANKS)` fonksiyonuna çıkar (para==TRY + bilgi dolu; aktif YOK) + characterization testi (test_midas_dus_buton). Kural: filtre koşulu, bayrağın GERÇEK anlamıyla eşleşmeli; "aktif" gibi çok-amaçlı görünen bayrağı yeni bir kapıya koymadan önce "bu bayrak tam olarak neyi ifade ediyor?" diye sor (#42/#37 ailesi).

---
*Kaynak: Garanti Midas kaynak tuşu kayıp 2026-07-25 → midas_bildirim.midas_kaynak_banka_adlari + test*
