---
ureten: hafiza-yayinla
tip: ders
no: 33
etiketler: [ders, rulebook]
---

# Ders 33 — `pm2 restart` temiz kapanışı GARANTİ ETMEZ

**`pm2 restart` temiz kapanışı GARANTİ ETMEZ** — "Temiz kapanış tamamlandı" logu 3 restart'ın yalnız 1'inde çıktı; PM2 handler bitmeden process'i öldürüyor. Kapanışta state yazımına GÜVENME (kritik state olay anında yazılmalı). State'i elle yazman gerekiyorsa: `pm2 stop → yukle_state()+kaydet_state() → pm2 start` (kural #31 ile aynı disiplin).

---
*Kaynak: p2p-bot restart gözlemi 2026-07-15*
