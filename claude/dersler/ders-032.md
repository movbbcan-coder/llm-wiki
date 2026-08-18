---
ureten: hafiza-yayinla
tip: ders
no: 32
etiketler: [ders, rulebook]
---

# Ders 32 — Koruyucu (guard) yalnız BİRİKİMLİ veriyi korumalı — periyodik sıfırlanan alanı korursan sistemi KİLİTLERSİN.

**Koruyucu (guard) yalnız BİRİKİMLİ veriyi korumalı — periyodik sıfırlanan alanı korursan sistemi KİLİTLERSİN.** `p2p_state._KORUNAN`'a `gunluk_satis` konmuştu; o liste tasarımı gereği her gece sıfırlanır (`yukle_state` tarih filtresi + 22:00 özeti). Gece yarısı bellek 0 / disk dün-dolu olunca nöbetçi "kaza" sanıp yazımı reddetti; disk 0'a düşemediği için **reddetme kendini besledi** → bot **7,5 saat HİÇBİR state yazamadı** (14/07 20:45 → 15/07 04:08), sessizce. **Kural: "sayı yarıya düştü = kaza" sezgisi yalnız birikimli alanlar için geçerli; periyodik sıfırlanan alan guard'a GİRMEZ. Guard eklerken "bu alan meşru olarak boşalır mı?" diye sor.** Ayrıca: guard'ın reddi ERROR log'luyordu ama kimse bakmıyordu → sessiz kilit.

---
*Kaynak: kaza nöbetçisi kendi kilidi 2026-07-15 (defter göçü sırasında tesadüfen bulundu) → p2p_state._KORUNAN + test_state_kaza_nobetcisi.py*
