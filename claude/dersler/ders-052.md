---
ureten: hafiza-yayinla
tip: ders
no: 52
etiketler: [ders, rulebook]
---

# Ders 52 — Kullanıcı ayarı (ödeme süresi/limit/eşik) "mevcut kayıttan miras" alınıyorsa değişiklik sessizce geri döner — sabit SSOT'tan yaz.

**Kullanıcı ayarı (ödeme süresi/limit/eşik) "mevcut kayıttan miras" alınıyorsa değişiklik sessizce geri döner — sabit SSOT'tan yaz.** P2P ilan `paymentPeriod` üç yolda da `ilan.get("paymentPeriod","15")` idi: varsayılan 15 ama şablon/reaktivasyon kaynağı eski 30 dk'lık ilan olunca 30 geri geliyordu (canlı ölçüm: status=20 ilanların 6/9'u pp=30) → müşteri ödemeyince iptal için yarım saat bekleniyordu. CLAUDE.md "30→15 çekildi" yazıyordu, kod kısmen uyuyordu — **beyan ≠ davranış, canlı kaydı ölç.** Fix: `p2p_core.ODEME_SURESI_DK` SSOT + üç yolda miras kaldırıldı + invaryant testi (şablon 30 verse bile payload sabit; SAYIYI değil mirassızlığı kilitler). Kural: kullanıcı tercihi olan alan asla eski kayıttan türetilmez; `d.get(X, varsayilan)` deseni gördüğünde "X kullanıcı ayarı mı, kayıt verisi mi?" diye sor.

---
*Kaynak: ilan ödeme süresi 30 dk kalıntısı 2026-07-28 → p2p_core.ODEME_SURESI_DK + bybit_isler + dongu_bakiye + test_odeme_suresi.py*
