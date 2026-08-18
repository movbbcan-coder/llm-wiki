---
ureten: hafiza-yayinla
tip: ders
no: 88
etiketler: [ders, rulebook]
---

# Ders 88 — Aynı bankanın PDF'i ile Excel'i damgayı FARKLI yerde saklar; biri parse edilmezse o kaynak "damgasız" girer ve ÇİFT SAYIM doğar.

**Aynı bankanın PDF'i ile Excel'i damgayı FARKLI yerde saklar; biri parse edilmezse o kaynak "damgasız" girer ve ÇİFT SAYIM doğar.** Garanti ekranda **21.992 ₺** göründü, gerçek bakiye **10.997 ₺** idi (kullanıcı fark etti). Ekstre aslında doğru işlenmişti — son kayıt bakiyesi 10.997,22 ile birebir. Hata damgadaydı: Garanti'nin e-imzalı PDF'i belge anını etiket-hücre olarak değil CÜMLE İÇİNDE veriyor (*"18/08/2026 tarihi saat 05:00 itibarıyla 11/08/2026 - 19/08/2026 …"*), oysa `belge_damgasi` satır/hücre tabanlıydı (Excel için yazılmıştı, #40). PDF kayıtları `belge_ts=None` girdi → sistemin gördüğü en yeni damga **12 gün eski** kaldı → `beklenen_bakiye` "fotoğraf bayat" sanıp ekstrede ZATEN bulunan 4 satışı (10.995 ₺) bir daha ekledi. **Damganın YOKLUĞU, yanlış damga kadar tehlikeli: ikisi de aynı parayı iki kez saydırır** (#59'un kardeşi — orada damga yanlış seçilmişti, burada hiç yok). Dersler: (a) bir belge tipi için yazılan "as-of" parse'ı, aynı bankanın DİĞER dosya biçimine otomatik geçmez — her biçim ayrı ayrı doğrulanmalı; (b) düzeltmeden sonra yeniden ingest YETMEZ, dedup yeni kaydı reddeder → zenginleştirme dalı şart (#40'ta öğrenilmişti, burada işe yaradı: 3 PDF, 0 yeni, 11 kayıt zenginleşti); (c) hatayı yakalayan şey yine `defter/teshis` mutabakatı oldu — "ekran 21.992 vs zincir 10.997" satırı kök nedeni tek bakışta verdi (#41). KALICI KAPI: canlı dosyaya karşı invaryant — *bir bankanın en yeni belge damgası, en yeni işlem tarihinden eski olamaz*.

---
*Kaynak: Garanti PDF belge damgası 2026-08-18 → parsers.belge_damgasi_metin + parse_pdf iliştirme + test_ekstre_zaman_ekseni +6*
