---
ureten: hafiza-yayinla
tip: ders
no: 62
etiketler: [ders, rulebook]
---

# Ders 62 — Bir öneri motoru dış dünyanın SERT kısıtını "uyarı" seviyesinde tutuyorsa, o öneri er ya da geç gerçek hesapta patlar — kısıt, arama uzayının İÇİNDE eleme olmalı.

**Bir öneri motoru dış dünyanın SERT kısıtını "uyarı" seviyesinde tutuyorsa, o öneri er ya da geç gerçek hesapta patlar — kısıt, arama uzayının İÇİNDE eleme olmalı.** veles_x optimizer'ı ADA için "mart %22 × 60 emir" önerdi; martingale çarpan toplamı (1,22^60 zinciri) **690.501** olduğu için ilk emir toplam hacmin 1/690.501'i = **0,0009 $ = 0,005 ADA** çıkıyordu. Bybit ADAUSDT `minOrderQty=1, qtyStep=1` → emir adım tabanına yuvarlanınca **0 adet**; gerçek Veles botu "Объём ордера не соответствует требованиям" ile ERROR'a düştü ve kullanıcı 120 gündür çalışan botu (ada long, mart %6 → ilk emir 23 ADA) durdurmuş olduğu için **sistem tamamen durdu** (Sheets kaydı da kesildi). Sim ekranı bunu ZATEN kırmızı yazıyordu ("İlk emir 0.0051 $") — ama yalnız uyarıydı; `optimizer/scorer.py` sadece likidasyona bakıyor, `PARAM_SPACE` martingale'i %50'ye kadar açıyordu. **İKİNCİ ders — sert kapı da yanlış yerden kurulabilir:** refleks eşik "Bybit min notional 5 $" idi; canlı kanıt (`veles_user_settings.json`: dep 22 ×10, mart %6 → ilk emir 0,41 $) o eşiğin ALTINDA 120 gün çalışmıştı → 5 $'ı sert kapı yapmak KANITLANMIŞ ayarı elerdi. Doğru ayrım: **min_qty = SERT (borsada var olamaz), min_notional = YUMUŞAK uyarı** (#34/#35 ailesi: kanıtlanmamış öncülle hüküm kurma). ÜÇÜNCÜ: aynı kavramın iki yolu vardı (pipeline in-process + search subprocess) → kapı ikisine de kondu, ikisi de ayrı mutasyonla kilitlendi (#41/#45). DÖRDÜNCÜ: yeni testler `optimizer/results/`'a canlı dosya yazdı → `tests/conftest.py` yoktu, eklendi (#30 birebir tekrarı).

---
*Kaynak: veles_x optimizer ayarı gerçek Veles botunu ERROR'a düşürdü 2026-08-03 → grid_math.SembolFiltre/emir_uygulanabilir_mi/plan_uygulanabilir_mi + exchange_filters.py + optimizer/uygunluk.py + scorer infeasible + pro.html sert banner + tests/test_uygulanabilirlik.py (23) + tests/conftest.py + engine.open_cycle kapısı (market girişinden ÖNCE: yarım grid = korumasız pozisyon) + pipeline arama uzayı ön-budama (17.280 kombonun %45'i borsada kurulamıyormuş)*
