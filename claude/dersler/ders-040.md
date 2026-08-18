---
ureten: hafiza-yayinla
tip: ders
no: 40
etiketler: [ders, rulebook]
---

# Ders 40 — Bir fotoğrafın damgası "içindeki son olayın" değil, "ne zaman çekildiğinin" damgasıdır — ve bunu tahmin etme, belgeye SOR.

**Bir fotoğrafın damgası "içindeki son olayın" değil, "ne zaman çekildiğinin" damgasıdır — ve bunu tahmin etme, belgeye SOR.** Ekstre bakiyesinin fotoğraf ts'i iki kez uyduruldu: önce gün sonu (`23:59` → fotoğrafı GELECEĞE taşır, o gün gelen satışları yutar), sonra son işlem saati (`06:08` → belgenin indirilmesine kadar geçen süreyi kaybeder). İkincisi CANLI REGRESYON yaptı: `get_dashboard_data`'nın Midas cutoff'u (`06:42` = SS'in İŞLENME anı) fotoğrafı bayat ilan edip **187,28 ₺'yi sıfırladı**; birinci uydurma bu hatayı tesadüfen maskeliyormuş (**bir hatayı düzeltmek, onun maskelediği hatayı ortaya çıkarır — "düzelttim" demeden önce AŞAĞI AKIŞI ölç**). Doğru cevap belgenin kendi beyanıydı: İş "Belge Düzenleme Tarihi 06:53:48", Garanti "İndirme Tarihi 06:58". **Kural: dış kaynaktan gelen fotoğrafın as-of damgası varsa PARSE ET; yoksa None bırak, türetme.** Yan dersler: (a) etiket sütunu bankaya göre kayar (İş 6→9, Garanti 0→1) → indeks sabitleme, etiket ara; (b) **dedup'lu ingest'e yeni ALAN eklemek işe yaramaz** — aynı belge iki yoldan gelir (Gmail+elle), ikincisi hep 0-yeni olur → zenginleştirme dalı şart (yalnız EKSİK alan, para verisi asla).

---
*Kaynak: İş Bankası 187,28→0 regresyonu 2026-07-21 → parsers.belge_damgasi + ingest zenginleştirme + ozet belge_ts*
