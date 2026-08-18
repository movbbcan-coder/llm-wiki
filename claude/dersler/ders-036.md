---
ureten: hafiza-yayinla
tip: ders
no: 36
etiketler: [ders, rulebook]
---

# Ders 36 — Aynı Midas çıkışı İKİ mekanizmayla düşülünce banka SIFIRLANIR — bildirim fotoğrafı zaten net.

**Aynı Midas çıkışı İKİ mekanizmayla düşülünce banka SIFIRLANIR — bildirim fotoğrafı zaten net.** Enpara giden-transferde kendi bakiyesini haber verir ("…1.600,25 TL… İşlem sonrası bakiye: 193 TL") → `guncel_bakiyeler` fotoğrafı 193'e (Midas ZATEN düşülmüş) taşır. Ama `midas_cikis.uygula` aynı 1600.25'i BİR DAHA düşüyordu çünkü buton çıkış-kaydının ts'i (04:20:38) bildirim ts'inden (04:20:37, foto dakikaya yuvarlanınca 04:20:00) sonra → strict `c_dt<=foto` "görülmemiş" sanıp düştü → `max(0,193−1600)=0`. **Kural: bir bankanın RAPORLADIĞI bakiye (bildirim fotoğrafı) o ana kadarki transferleri zaten netler; midas_cikis yalnız bildirim-fotoğrafına MUTABAKAT TOLERANSI uygulamalı (İş/Garanti gibi bildirimsiz banka strict kalır).** İKİNCİ tuzak: P2P tarafı (`ekstre_harcama.gercek_bakiye`) `bakiye_kaynak`'ı midas_cikis'e TAŞIMIYORDU → tolerans kapısı orada tetiklenmedi, Finans düzelip P2P 0'da kaldı (kaynak-alanı taşınmazsa SSOT fix yarım kalır).

---
*Kaynak: Enpara 193→0 çift-düşüm 2026-07-16 → midas_cikis.BILDIRIM_MUTABAKAT_TOL + ekstre_harcama bakiye_kaynak + test_midas_cikis.py*
