---
ureten: hafiza-yayinla
tip: ders
no: 39
etiketler: [ders, rulebook]
---

# Ders 39 — Append-only deftere "ters kayıt" yazmadan önce tüketicinin işareti nasıl okuduğuna bak.

**Append-only deftere "ters kayıt" yazmadan önce tüketicinin işareti nasıl okuduğuna bak.** 5.575,90 ₺'lik satış yanlış bankaya yazılmıştı; refleks çözüm "Garanti'ye −5.575,90, İş'e +5.575,90 ekle" idi. BOZUK olurdu: `beklenen_bakiye._defter_hareketleri` `satis` tipini `abs(tutar)` + `yon="in"` diye okuyor → negatif satış bakiyeyi DÜŞÜRMEZ, **ARTIRIR** (aynı parayı Garanti'ye ikinci kez eklerdi). Yanlış yazılmış bir olayın NİTELİĞİ (banka) yerinde düzeltilir + ayrı `hata` kaydıyla iz bırakılır (tutar=0 → hiçbir hesabı etkilemez); "append-only" dogması uğruna matematiği bozma. Ayrıca: banka kimliğini defter değil **ekstre çapraz doğrulaması** verdi (İş'te +5.576,00 var, Garanti'de aynı pencerede hiç yok) — #29'un kardeşi: kimlik metinden/rotasyondan değil, iki bağımsız kaynağın kesişiminden çıkar.

---
*Kaynak: P2P satış banka ataması 2026-07-21 → banka_hareket.json duzeltme:banka:* izi*
