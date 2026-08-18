---
ureten: hafiza-yayinla
tip: ders
no: 27
etiketler: [ders, rulebook]
---

# Ders 27 — p2p-bot restart'ı ÇİFT yan-etki tetikler:

**p2p-bot restart'ı ÇİFT yan-etki tetikler:** (1) startup [RESTORE] `aktif_siparis`'teki tamamlanmış siparişleri havuza GERİ YAZAR (dedup son-500 sınırlı → eski sipariş tekrar yüklenir, havuz şişer: 6K→54K); (2) `aed_ilan_bakim` startup görevi `aed_aktif=True` görünce kapalı AED ilanını REAKTİVE eder (kullanıcı açmadığı halde AED siparişi gelir). **Ders: p2p-bot'u gereksiz restart etme; restart gerekiyorsa önce [RESTORE] guard + AED opt-in aktif olsun.** Fix: trading/restore_guard.py (createDate≤24s gate) + aed_aktif default False

---
*Kaynak: havuz+AED çift-şişme 2026-07-13 (benim pool-fix restart'ım tetikledi) → restore_guard.py + aed_aktif opt-in*
