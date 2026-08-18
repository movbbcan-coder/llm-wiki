---
ureten: hafiza-yayinla
tip: ders
no: 31
etiketler: [ders, rulebook]
---

# Ders 31 — Bakım script'i `p2p_state`'i import ediyorsa MUTLAKA `yukle_state()` çağır.

**Bakım script'i `p2p_state`'i import ediyorsa MUTLAKA `yukle_state()` çağır.** `state` modül-seviye VARSAYILAN (boş) dict'tir; yüklemeden `kaydet_state()` çalışırsa DİSK EZİLİR. Canlı hasar: 320,85 USDT transit + alım kayıtları silindi, `islenen_siparis_ids` (dedup) uçtu → restart'ta [RESTORE] 14 siparişi geri yükledi → havuz 6.4K→19.6K şişti. **Ayrıca: bot ÇALIŞIRKEN state dosyasını elle düzeltme — bellekteki eski hâl diski ezer; `pm2 stop → düzelt → pm2 start`.** Fix: p2p_state._yazim_guvenli_mi() kaza nöbetçisi (diskteki kayıt sayısı yarıya düşüyorsa yazımı REDDEDER)

---
*Kaynak: state ezilmesi 2026-07-14 → p2p_state.py + test_state_kaza_nobetcisi.py*
