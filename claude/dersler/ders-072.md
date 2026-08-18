---
ureten: hafiza-yayinla
tip: ders
no: 72
etiketler: [ders, rulebook]
---

# Ders 72 — Elle `Migration` yazarken SQL'i gözle değil, Room'un dışa aktardığı şemadan al — ve yıkıcı göç kancasının hâlâ takılı olup olmadığını ÖNCE ölç.

**Elle `Migration` yazarken SQL'i gözle değil, Room'un dışa aktardığı şemadan al — ve yıkıcı göç kancasının hâlâ takılı olup olmadığını ÖNCE ölç.** Denk'e varlık tablosu eklerken iki tuzak arka arkaya çıktı: (a) `fallbackToDestructiveMigration()` hâlâ açıktı, yani sürümü 6→7 yapmak telefondaki **19 hareketlik gerçek defteri sessizce silecekti** (ADR "yayından sonra gerçek göç" diyordu ama kanca sökülmemişti — belge ile kod ayrışmıştı); (b) elle yazdığım `CREATE TABLE`'da `aktif` sütununa `DEFAULT 1` koymuştum, Room varsayılan değeri de karşılaştırdığı için uygulama açılışta "Migration didn't properly handle" ile çökerdi. İkisi de `app/schemas/<db>/7.json` içindeki `createSql`'i okuyarak, cihaza hiç dokunmadan yakalandı. **Kural: şema sürümü artıran her değişiklikte önce `fallbackToDestructive*` var mı diye bak (varsa KALDIR — çökmek, sessizce silmekten iyidir), sonra migration SQL'ini exported schema JSON'undan birebir kopyala.** Doğrulama kapısı: gerçek v(n-1) veritabanı olan cihazda aç, kayıt sayısını ÖNCE/SONRA karşılaştır (Room şemayı açılışta doğruladığı için sorgu dönüyorsa tablo/sütun birebir eşleşmiş demektir).

---
*Kaynak: Denk KARAR FAZ 2 varlık tablosu 2026-08-09 → Sema.GOC_6_7 + addMigrations*
