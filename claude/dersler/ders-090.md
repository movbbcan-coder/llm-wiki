---
ureten: hafiza-yayinla
tip: ders
no: 90
etiketler: [ders, rulebook]
---

# Ders 90 — Alıcının O AN yapabileceği bir şey yoksa uyarı gönderilmemeli — "durum" ile "olay" ayrı şeylerdir; aralığı seyreltmek gürültüyü çözmez.

**Alıcının O AN yapabileceği bir şey yoksa uyarı gönderilmemeli — "durum" ile "olay" ayrı şeylerdir; aralığı seyreltmek gürültüyü çözmez.** #82'de tünel nöbetçisinin sabit 30 dk'lık tekrarı artan aralığa (30 dk → 2 sa → 8 sa → günde bir) çevrilmişti; kullanıcı beş gün sonra yine şikâyet etti: *"kullanılmadığı zamanda koptu diye bildirimle boğmasın"*. Çünkü asıl hata sıklıkta değil ÖNCÜLDEYDİ: nöbetçi "tünel kopuk" durumunu haber sanıyordu. Telefon boştayken tünelin kopuk olması kullanıcı için bir olay değildir — yapacağı bir şey yok, bilse de bir şey değişmez. Haber ancak tünel **lazım olduğunda ve yokken** doğar. Fix: talep tabanlı nöbet — araçlar (`tel`/`telss`/`otogor`) tüneli kullanmaya çalışıp **taşıma katmanında** başarısız olunca (`ssh` 255 / `timeout` 124; uzak komutun kendi hata kodu SAYILMAZ, o tünelin sağlam olduğunu kanıtlar) `veri/tunel_talep` işaretini bırakır; nöbetçi ölçmeye devam eder ama yalnız bekleyen ihtiyacın üstüne konuşur ve işareti TÜKETİR. Üç incelik teste bağlandı: (a) gönderim başarısızsa ihtiyaç tüketilmez (duyurulamamış ihtiyaç hâlâ bekliyordur, #80); (b) tünel düzelince ihtiyaç her hâlükârda temizlenir, yoksa bir sonraki kopmada eski talep "şu an lazım" diye okunur; (c) **haberi verilmemiş arızanın düzelmesi müjde değildir** — "geri geldi" bildirimi kesilen gürültüyü arka kapıdan geri getirirdi. Ayrıca işareti kabuk yazıp Python okuduğu için yol+alan adları iki dilde kilitlendi (#84: yanlış alan adı = sessiz kapalı kapı). **Genel biçim: bir bildirim tasarlarken "bunu alan kişi şu an ne yapacak?" diye sor; cevap "hiçbir şey" ise o bildirim yoktur.**

---
*Kaynak: ccoto tünel bildirimi ikinci şikâyet 2026-08-21 → tunel.ihtiyac_isaretle/bekleyen_ihtiyac + tel_ortak.tel_ssh rc kapısı + tests/test_tunel.py (22) + tests/conftest.py*
