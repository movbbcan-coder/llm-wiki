---
ureten: hafiza-yayinla
tip: ders
no: 38
etiketler: [ders, rulebook]
---

# Ders 38 — Bir koruyucu, öncülünün geçerli OLMADIĞI girdiye de uygulanırsa gerçek parayı siler — kapsamı öncülle aynı olmalı.

**Bir koruyucu, öncülünün geçerli OLMADIĞI girdiye de uygulanırsa gerçek parayı siler — kapsamı öncülle aynı olmalı.** `havuz_otoritesi`'nin öncülü: *"ekstre tabanı eski, üstüne yalnız GELEN bildirim binmiş → şişer"*. Ama kapsamı `kaynak.startswith("ekstre")` idi → **saf ekstreyi de** kırpıyordu. Saf ekstre bankanın kendi kapanış bakiyesidir (girişi de çıkışı da içerir, şişemez): İş Bankası ekstresi 21.07 06:53'te indi, 06:08'deki 17.700 ₺ Midas çıkışını İÇERİYORDU, kalan 187,28 ₺ gerçekti — havuz 0 olduğu için ekran **0,00 ₺** gösterdi (#32/#35'in aynısı: öncülü tutmayan koruyucu yanlış hüküm verir). Kapsam `ekstrapolasyonlu()` ile öncüle eşitlendi. **İKİNCİ ders — düzeltmenin ilk denemesi de yanlış öncüle dayanıyordu:** "fotoğraf son çıkıştan yeniyse kırpma" yazdım, tetiklenmedi çünkü defterdeki çıkış damgası **paranın çıktığı an değil SS'in işlendiği an** (06:22 vs 06:08). Damga kıyasını yazmadan önce "bu damga neyin zamanı?" diye sor (#28'in kardeşi). **ÜÇÜNCÜ:** aynı olguya iki defter bakıyorsa (`banka_hareket.json` midas_dus + `dashboard/midas_cikis.json`) ve bir yol yalnız birine yazıyorsa (SS yolu), ekran katmanı kör kalır — SSOT ihlali.

---
*Kaynak: İş Bankası 187,28→0 + ekstre zaman ekseni 2026-07-21 → havuz_otoritesi.ekstrapolasyonlu + ozet._zincir_sonu + test_ekstre_zaman_ekseni.py*
