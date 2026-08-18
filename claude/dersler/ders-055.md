---
ureten: hafiza-yayinla
tip: ders
no: 55
etiketler: [ders, rulebook]
---

# Ders 55 — Aynı olayı iki kaynak yazıyorsa dedup kapısını İKİ YÖNDE de kapat — tek yön kapatılırsa hata sadece sıraya bağlı olarak ortaya çıkar (sinsi).

**Aynı olayı iki kaynak yazıyorsa dedup kapısını İKİ YÖNDE de kapat — tek yön kapatılırsa hata sadece sıraya bağlı olarak ortaya çıkar (sinsi).** Denk'te kartla ödenen alışveriş hem banka bildirimi hem fiş olarak geliyordu (R-FIS-2). İlk refleks yalnız "fiş, bildirimi arasın" idi; ama kullanıcı fişi önce eklerse (nakit sanıp) bildirim yine ikinci gider açardı → aynı hata, sadece sırası değişik. Fix: tek saf kapı (`FisEslestirme.bul`) + iki çağrı yeri (fisEkle → kaynak=bildirim ara, bildirimIsle → kaynak=fiş ara), kayıt tek kalır ("tek işlem, iki kanıt"). İKİNCİ DERS — eşiği verinden ölç: "tutar tam eşit olmalı" refleksi yanlıştı, P2P canlı verisinde 527,25 bildirim ↔ 527,00 fiş AYNI alışverişti (tolerans şart), ama sabit 50 kuruş küçük tutarda saçmalar → tolerans tutarın %10'unu aşmaz. ÜÇÜNCÜ — sessiz dedup da kötüdür: yanlış eşleşme harcamayı YUTAR; ekran kararı söyler + "ayrı harcama" seçeneği sunar. DOĞRULAMA: iki kapı da mutasyonla tek tek kapatıldı, ilgili test anında kırmızıya döndü (kilit vacuous değil).

---
*Kaynak: Denk fiş↔bildirim çift sayımı 2026-07-29 → domain/FisEslestirme + Defter.fisEkle/bildirimIsle + DefterFisTest (8 vaka)*
