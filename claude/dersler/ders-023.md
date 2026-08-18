---
ureten: hafiza-yayinla
tip: ders
no: 23
etiketler: [ders, rulebook]
---

# Ders 23 — Deposit geçmişi değişen botta getiri oranı SABİT deposit'e bölünmez — her günün

Deposit geçmişi değişen botta getiri oranı SABİT deposit'e bölünmez — her günün take_home'u o gün geçerli deposit'e (DEPOSIT_HISTORY) bölünmeli; yoksa eski dönem oranları kat kat düşük çıkar (24$→150$ geçişi = 6.25× sapma). DİKKAT: fix sadece simulate()'e uygulanırsa Sheets "Sermaye Projeksiyonu" hâlâ yanlış kalır — build()/build_monthly/build_weekly/build_summary'nin ürettiği daily_return_pct/cum_return_pct de aynı resolver'ı kullanmalı (Sheets tabı bu yüzdelerden çiziliyor)

---
*Kaynak: veles Sermaye Projeksiyonu 2026-06-13 → daily_stats.py make_deposit_resolver + build() resolver (2026-06-13)*
