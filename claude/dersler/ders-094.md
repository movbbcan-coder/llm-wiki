---
ureten: hafiza-yayinla
tip: ders
no: 94
etiketler: [ders, rulebook]
---

# Ders 94 — Her girdiyi "önce X mi?" diye deneyen bir boru hattı, X OLMAYANLAR için yanlış alarm üretir — ve o gürültü gerçek arızayı gizler.

**Her girdiyi "önce X mi?" diye deneyen bir boru hattı, X OLMAYANLAR için yanlış alarm üretir — ve o gürültü gerçek arızayı gizler.** Gmail ajanı her PDF eki önce ekstre olarak deniyor; fatura/makbuz/ödeme-hatırlatma da bu yoldan geçip "⚠️ Ekstre işlenemedi" bildirimi üretiyordu (canlı: `Invoice-*`, `Receipt-*`, `Payment Warning/Reminder`). Aynı mesajın içinde GERÇEK bir arıza saklıydı: **ADCB (BAE Bankası) ekstresi parola korumalı PDF** (`pdftotext: Incorrect password`) → metin çıkmıyor → o hesap **2 Temmuz'dan beri** kayıt almıyor, bakiyesi 49 AED'de donmuş. Yani gürültü, sinyali gömmüştü (#82'nin ikinci yüzü: yanlış alarm sadece rahatsız etmez, gerçek alarmı da değersizleştirir). Fix, ayrımı DOĞAL yere kurarak: belgeden **metin çıktıysa** o bir faturaydı, okundu → alarm geri alınır; **metin çıkmadıysa** (şifreli/taranmış) → alarm kalır. Ek uyarı: yeni bir "başarı bildirimi" eklerken sessizlik koşulunu da yaz — özet yalnız YENİ kayıt varken gider, aynı ekstrenin tekrarında (0 yeni) susar; yoksa günde birkaç kez gelen aynı mesaj kanalı çöpe çevirir. YAN DERS (SSOT): bildirimdeki "banka · son bakiye" alanları ingest'te (kanonik kayıt sahibi) üretildi; çağıran depoyu kendi okusaydı ikinci bir "son bakiye" hesabı doğardı — bu depoda en sık tekrar eden hata sınıfı (#45). ÖLÇÜM NOTU: "ekstrelerim işleniyor mu?" sorusu ancak **hesap bazında tazelik tablosu** ile cevaplanır (her banka için son işlem tarihi + en yeni belge damgası); "ajan çalışıyor" veya "son mail işlendi" demek yetmez — 4 bankadan 3'ü güncelken biri 7 haftadır kördü ve hiçbir toplam bunu göstermiyordu.

---
*Kaynak: Gmail ekstre boru hattı denetimi 2026-08-23 → attachment_handler._pdf_metin bool + yanlış-alarm geri alma · main.py başarı özeti · ekstre/ingest.py rapor özet alanları · test_attachment_ekstre (9) + test_ekstre_pdf (9)*
