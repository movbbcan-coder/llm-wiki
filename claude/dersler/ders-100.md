---
ureten: hafiza-yayinla
tip: ders
no: 100
etiketler: [ders, rulebook]
---

# Ders 100 — "Yeni kayıt yok" ile "aynı belge tekrar geldi" ayrı hâllerdir — ikisini aynı sessizliğe koyarsan kullanıcı sistemin çalışmadığını sanır.

**"Yeni kayıt yok" ile "aynı belge tekrar geldi" ayrı hâllerdir — ikisini aynı sessizliğe koyarsan kullanıcı sistemin çalışmadığını sanır.** Kullanıcı İş Bankası ekstresini Gmail'e attı ve "mail agent onu okumadı, Garanti'yi okudu" dedi. Ölçüm: ajan İKİSİNİ DE okumuştu — İş Bankası 7 satır **yeni=0**, Garanti 20 satır yeni=3. İş Bankası'nın o 7 hareketi iki gün önceki ekstreyle zaten kaydedilmişti (aradan hareket geçmemiş), veri de doğruydu: iki ekran da 14.892,71 ₺ gösteriyordu. Eksik olan TEYİTTİ: 2026-08-23'te koyduğum "0 yeni ise sus" kuralı (tekrar gürültüsünü önlemek için doğru bir kural) burada yanlış tarafa düştü ve **çalışan sistem çalışmıyor gibi göründü**. Fix: ingest raporuna `belge_yeni` (belgenin KENDİ damgası depoda ilk kez mi görülüyor) → ajan "yeni kayıt VAR **ya da** belge yeni" ise konuşur, aynı belgenin tekrar yüklenmesinde susar; mesaj da ayrışır: "✅ Ekstre işlendi — 3 yeni kayıt" / "📄 Ekstre okundu — yeni hareket yok, kayıtlar zaten güncel". Kural: **sessizlik tasarlarken "kullanıcı bu eylemi BİLEREK yaptı mı?" diye sor** — kullanıcının gönderdiği her belge en az bir kez teyit hak eder; susulacak olan, sistemin kendi tekrarıdır. YAN DERS (üçüncü kez aynı hata): kapıyı önce kaynak-metin testiyle kilitledim, `belge_yeni = False` mutasyonu YAKALANMADI — test satırın VARLIĞINA bakıyordu, SONUCUNA değil. Gerçek ekstre dosyasıyla geçici depoya iki kez ingest eden davranışsal teste çevrilince hem `False` hem `True` mutasyonu kırmızıya döndü. **Kaynak-metin kilidi ancak davranışı ölçemediğinde kabul edilir; ölçebiliyorsan davranışı ölç.**

---
*Kaynak: Gmail ekstre teyidi 2026-08-28 → ingest.belge_yeni/belge_ts + gmail_agent bildirim kuralı + test_ekstre_pdf (12, davranışsal)*
