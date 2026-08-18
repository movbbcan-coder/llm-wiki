---
ureten: hafiza-yayinla
tip: ders
no: 77
etiketler: [ders, rulebook]
---

# Ders 77 — Kabuk zinciri elle birleştirilirse sonda kalan ayraç TÜM zinciri sessizce iptal eder.

**Kabuk zinciri elle birleştirilirse sonda kalan ayraç TÜM zinciri sessizce iptal eder.** `otogor` ön zinciri `input keyevent 4; sleep 1;` diye kuruyordu; telefonda `…; ; rm -f` olunca sh **sözdizimi hatası** verip zinciri hiç koşmadı → geri tuşu basılmadı, `am start` çalışmadı. Arıza görünmedi çünkü yeniden deneme dalı (ön zinciri tekrarlamadan) geçerli bir döküm üretiyordu: çıktı sağlıklı, davranış yok. İki tur "geri tuşu neden çalışmıyor" tahmini yürütüldü. **Kural: komut zinciri kompozisyonu SAF bir fonksiyonda toplanır ve testi `sh -n` ile SÖZDİZİMİNİ kilitler (sayıyı değil).** Aynı test bozuk biçimin gerçekten reddedildiğini de kanıtlamalı, yoksa kapı vacuous olur (#41).

---
*Kaynak: ccoto FAZ 0 2026-08-12 → tel_ortak.tel_zincir_kur + tests/test_zincir.sh*
