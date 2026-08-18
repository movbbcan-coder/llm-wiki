---
ureten: hafiza-yayinla
tip: ders
no: 85
etiketler: [ders, rulebook]
---

# Ders 85 — "Alfanümerik mi" ile "ASCII mi" AYRI sorulardır — homoglif (göze aynı görünen Yunan/Kiril harf) tüm imzayı sessizce bozar ve denetimin kendisi 'temiz' der.

**"Alfanümerik mi" ile "ASCII mi" AYRI sorulardır — homoglif (göze aynı görünen Yunan/Kiril harf) tüm imzayı sessizce bozar ve denetimin kendisi 'temiz' der.** Kullanıcı ikinci Bybit hesabının anahtarını yapıştırdı, imza sürekli `10004 Error sign` verdi. Denetimim "uzunluk 18/36 doğru, boşluk yok, **alfanümerik-dışı karakter yok** → yapıştırma temiz" dedi ve teşhis üç tur yanlış yöne gitti (önce yanlış yapıştırma, sonra Demo/Testnet ortamı, sonra "secret o key'e ait değil"). Gerçek sebep: secret'ın 8 karakteri **Yunan büyük harfiydi** (Υ U+03A5, Γ, Α, Ζ, Ρ, Ο) — ekranda `Y G A Z P O` ile birebir aynı görünüyor. `isalnum()` Unicode'da bunlara **True** döndüğü için kapı hiç kapanmadı; doğru kontrol `isascii()`/`ord(c)>127` idi. Kaynağı büyük olasılıkla ekran görüntüsünden OCR ile okumaktı ve **kopya kurtarılamıyor**: homoglifleri Latin karşılıklarına çevirip denedim, yine `Error sign` — OCR aynı anda `0↔O`, `1↔l`, `5↔S` gibi başkalarını da bozmuş oluyor. **Kural: dış dünyadan gelen kimlik/sır dizgilerinde (API anahtarı, IBAN, token, imza) 'geçerli karakter' kontrolü ASCII tabanlı olmalı; Latin-dışı tek karakter bile kopyayı GEÇERSİZ sayıp kaydı REDDETMELİ ve sebebi (hangi pozisyon, hangi harf) kullanıcıya söylemeli** — "kullanım hatası" demek, kullanıcıyı doğru yapıştırdığına inandırıp saatler yakar. YAN DERSLER (aynı turda): (a) iki cüzdanın hatası tek `hata` değişkeninde tutulduğu için ikincisi birincisini eziyordu → kullanıcı yalnız FUND hatasını gördü, UNIFIED'in sebebi kayboldu (hataları BİRİKTİR); (b) `wallet-balance` artık yalnız UNIFIED kabul ediyor ("accountType only support UNIFIED"), FUND ayrı varlık ucundan okunur — yanlış uç seçimi "imza sorunu" gibi görünür; (c) kullanıcı sırrı sohbete yapıştırdı (oturum diske düşüyor + özeti üçüncü tarafa gidiyor) → sır alma yolu ürünün İÇİNDE olmalı (`/bybit2` komutu: mesajı siler, maskeli yanıt, .env'e atomik yazım).

---
*Kaynak: Bybit#2 anahtarı Error sign 2026-08-16 → bybit2_komut.ascii_disi + girdi_ayikla reddi + hata biriktirme + cuzdan_bakiye_ham FUND ucu + test_bybit2_komut (25)*
