---
ureten: hafiza-yayinla
tip: ders
no: 28
etiketler: [ders, rulebook]
---

# Ders 28 — Para havuzunda ZAMAN EKSENİ yoksa her düşüm süpürmedir.

**Para havuzunda ZAMAN EKSENİ yoksa her düşüm süpürmedir.** `banka_bakiye.json` düz `{banka: float}` idi → Midas SS'i "en dolu bankadan süpür + cutoff=now" yapıyordu; SS'in kendi TARİH'i (Midas emir saati) parse ediliyor ama KULLANILMIYORDU. Sonuç: SS'i geç atınca araya giren satışın parası uçuyordu (01:04 emir → 01:42 satış 1.500₺ → 08:02 SS → süpürüldü; 4.810₺ kalan sessizce atıldı). **Kural: para düşen her işlemde cutoff = PARANIN ÇIKTIĞI AN, "şimdi" değil; düşülemeyen tutar sessizce atılmaz, raporlanır.** Fix: banka_havuzu/hareket.py (append-only defter) + trading/midas_dusum.py (tek kapı, çift-düşüm guard'ı, per-banka cutoff)

---
*Kaynak: Midas SS zaman-körlüğü 2026-07-14 → midas_dusum.py*
