---
ureten: hafiza-yayinla
tip: ders
no: 54
etiketler: [ders, rulebook]
---

# Ders 54 — Bir rakamı kıyaslamadan önce "bu rakam TAM OLARAK neyin ölçüsü?" diye sor — satır toplamı fiyat DEĞİLDİR.

**Bir rakamı kıyaslamadan önce "bu rakam TAM OLARAK neyin ölçüsü?" diye sor — satır toplamı fiyat DEĞİLDİR.** Denk fiyat hafızası (fiş ürün kıyası) yazılırken refleks çözüm "aynı ürünün geçen tutarıyla bugünküyü kıyasla" idi; P2P'nin gerçek fiş verisi bunu çürüttü: `ULKER BITTER CIKOLAT` 67,80 → 84,75 → 118,65 → 107,40, fiyat hiç değişmemiş, ADET değişmiş (3'lü/5'li alım). Satır toplamını fiyat sanan hafıza kullanıcıya "%75 zam" diye yalan söylerdi ve bir daha inanılmazdı. Fix: kalem, adet çarpanını (`3 X 36,00`, `0,850 KG X 29,90`) ayrı okur → **birim fiyat** üretir; çarpan okunamazsa `adetKesin=false` işaretlenir ve %60 üstü sıçrama SÖYLENMEZ (susmak, yanlış söylemekten iyidir). Aynı aile: #28/#40 ("bu damga hangi olayın zamanı?"), #48 ("bu bayrak tam olarak neyi ifade ediyor?"). YAN DERS: kural yazmadan önce kendi deponda gerçek veri ara — 21 satırlık `fis_harcama.json` bir tasarım hatasını doğmadan öldürdü.

---
*Kaynak: Denk fiyat hafızası 2026-07-29 → leaf/FisOkuyucu.Kalem + domain/FiyatHafizasi + 30 test*
