---
ureten: hafiza-yayinla
tip: ders
no: 29
etiketler: [ders, rulebook]
---

# Ders 29 — Belge metninden kimlik çıkarma kırılgandır; IBAN kesindir.

**Belge metninden kimlik çıkarma kırılgandır; IBAN kesindir.** Garanti PDF'i banka adını başlıkta değil 6.632. karakterdeki dipnotta geçiriyor → `metin[:4000]` taraması bulamadı → kayıtlar `banka or "?"` ile girdi. id hash'ine banka girdiği için aynı işlem "Garanti" ve "?" olarak İKİ id aldı → dedup kaçtı → gelir/gider çift sayıldı, "? 8₺" hayalet hesabı iki dashboard'un toplamına sızdı. **Kural: TR ekstresinde banka kimliği IBAN'dan çözülür (5-9. hane = EFT kodu); metin imzası yalnız ilk denemedir. IBAN'ı da normalize et — regex komşu metinden hane yutuyor.**

---
*Kaynak: Garanti "?" hesabı 2026-07-14 → banka_norm.iban_banka/iban_temizle*
