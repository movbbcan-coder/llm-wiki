---
ureten: hafiza-yayinla
tip: ders
no: 45
etiketler: [ders, rulebook]
---

# Ders 45 — Aynı "gerçek bakiye" iki ekrana AYRI kod yollarıyla çıkıyorsa, bir düzeltme yalnız birine uygulanır ve ekranlar sessizce ayrışır — mantığı ORTAK fonksiyona çıkar.

**Aynı "gerçek bakiye" iki ekrana AYRI kod yollarıyla çıkıyorsa, bir düzeltme yalnız birine uygulanır ve ekranlar sessizce ayrışır — mantığı ORTAK fonksiyona çıkar.** İş Bankası kart harcaması (fiş, bildirimsiz banka) P2P dashboard'da bakiyeden düşülüyordu ama Finans dashboard'da düşülmüyordu (get_finans_data'nın bakiye zincirinde o katman yoktu) → İş Bankası P2P'de 2.049 Finans'ta 2.187, kullanıcı "fiş düşmedi" dedi. Kök: fiş-düşme mantığı get_dashboard_data'ya GÖMÜLÜYDÜ, ortak değildi. Fix: `gorunmeyen_dusum` fonksiyonuna çıkarıldı, iki dashboard da çağırır. (Bu depoda tekrar eden sınıf: Enpara 3.805 vs 2.657, havuz_otoritesi ortaklaştırması, beklenen_bakiye — hepsi "kopya bakiye hesabı" ailesinden.) Kural: bir sayı birden çok ekranda görünüyorsa hesabı TEK fonksiyonda tut; "şu ekrana da ekle" refleksi kopyayı çoğaltır. YAN DERS: fiş kaydı Sheets'e bağımlıydı (token ölünce fiş hiç kaydolmadı, yerel yedek yok) — dış servise yazan kayıt önce yerele yazmalı (servis çökse de veri kalsın).

---
*Kaynak: fiş İş Bankası düşmedi 2026-07-24 → trading.fis_harcama.gorunmeyen_dusum + iki dashboard + test*
