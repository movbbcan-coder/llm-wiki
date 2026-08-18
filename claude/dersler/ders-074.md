---
ureten: hafiza-yayinla
tip: ders
no: 74
etiketler: [ders, rulebook]
---

# Ders 74 — `uppercase()` cihazın locale'ini kullanır — Türkçe arayüzde kendi dilini yanlış yazar.

**`uppercase()` cihazın locale'ini kullanır — Türkçe arayüzde kendi dilini yanlış yazar.** Denk'in bölüm etiketi "Düzenli yükün" → ekranda **"DÜZENLI YÜKÜN"** (noktasız I) çıktı; cihaz İngilizce locale'de çalışıyordu. Uygulamanın sabit dili Türkçe olduğu için büyütme de sabit olmalı: `uppercase(Locale("tr","TR"))`, tek yerde (`String.buyut()`), tüm etiketler ve widget oradan geçiyor. Testi Türkçe cihazda yazmak İŞE YARAMAZ — hatanın çıktığı hâl hiç kurulmaz; test `Locale.setDefault(Locale.US)` ile İngilizce cihazı ZORLUYOR (#35: denetlenmeyen hâl denetlenmiş sanılır). Ters yön de kilitli: "Varlık" → "VARLIK" (noktasız ı, noktasız I kalmalı).

---
*Kaynak: Denk etiket büyütmesi 2026-08-09 → Bilesenler.buyut + BuyutmeTest*
