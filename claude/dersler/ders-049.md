---
ureten: hafiza-yayinla
tip: ders
no: 49
etiketler: [ders, rulebook]
---

# Ders 49 — Fiş/görünmeyen-harcama cutoff'u bakiye "ts"si DEĞİL, ekstre BELGE tarihi olmalı — "ts" o banka için defter-satış tarihi olabilir.

**Fiş/görünmeyen-harcama cutoff'u bakiye "ts"si DEĞİL, ekstre BELGE tarihi olmalı — "ts" o banka için defter-satış tarihi olabilir.** İş bildirimsiz banka; fiş cutoff'u `beklenen_bakiye.ts` (07-25 = "+1 defter" satış tarihi) kullanıyordu, ekstre belge tarihi (07-21) değil. Fiş 07-24 ikisinin arasında → cutoff 07-25 fişi "zaten ekstrede" sanıp eledi → P2P İş=183, Finance=45 (Finance foto_ts=belge tarihi kullanıyordu → doğru). #45 ailesi: iki dashboard aynı gorunmeyen_dusum'u FARKLI snapshot'la çağırdı. Fix: `ekstre_belge_damgalari(eks)` saf helper (islemler.json belge_ts, en yeni) → P2P bildirimsiz banka snapshot'ını belge tarihiyle ezer; Finance zaten kullanıyor. Yan-bug: dashboard/fis_harcama.json köprüsü BOŞTU (Finance türev-yazması çalışmamış) → tazelendi. Ders: bir "damga"yı cutoff yapmadan önce "bu hangi olayın zamanı?" sor (#28/#40 kardeşi).

---
*Kaynak: İş P2P fiş cutoff 2026-07-26 → fis_harcama.ekstre_belge_damgalari + get_dashboard_data + test (1184)*
