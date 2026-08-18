---
ureten: hafiza-yayinla
tip: ders
no: 83
etiketler: [ders, rulebook]
---

# Ders 83 — Bir kayıt sistemi DOSYA ÜRETİYOR diye çalıştığını sanma — varlığı değil GERİ ÇAĞIRMAYI ölç.

**Bir kayıt sistemi DOSYA ÜRETİYOR diye çalıştığını sanma — varlığı değil GERİ ÇAĞIRMAYI ölç.** Oturum özetleyicisi (`auto_session_save.py`) 385 dosya üretmişti ve "çalışıyor" görünüyordu. Gerçek bir soruyla sınandı ("claude2 hangi karttan kesiliyor?"): **ham transcript'te 7 dosyada 0,17 sn'de bulundu, 385 özetin HİÇBİRİNDE yoktu.** Üç ayrı kök neden çıktı, üçü de sessizdi: (a) çağrılan model `gemini-2.0-flash-lite` Google tarafından KALDIRILMIŞTI (404 ölçüldü) — hata `stderr`'e yazılıp yutuluyor, araç mekanik dökme moduna düşüyordu; rulebook #44 bu dersi zaten yazmıştı ama yalnız vision-gateway'e uygulanmıştı (#45: aynı hata iki yerde, biri düzeltilip öteki unutulur); (b) `/root/.env`'deki `GEMINI_MODEL` daha da eski bir sürümü DAYATIYORDU — koddaki varsayılanı düzeltmek yetmedi, **yapılandırma düzeltmeyi eziyordu**; (c) özetleyici modele YALNIZ kullanıcı mesajlarını veriyordu, asistanın cevaplarını değil — yani bulguların yaşadığı yarıyı hiç görmüyordu. **Kurallar:** (1) üretilen çıktıyı gerçek bir soruyla sına, dosya sayısıyla değil; (2) bir aracın "zeki" adımı düşerse çıktının İÇİNE `⚠️ ÇALIŞMADI (sebep)` yaz — sessiz degradasyon aylarca fark edilmez; (3) sabit model/sürüm adı bir arıza noktasıdır, `*-latest` kullan; (4) kodu düzeltince aynı değeri dayatan ENV/config var mı diye bak. YAN DERS (aynı gün, aynı soruşturma): kayıt yeterliydi, eksik olan ARAMAYDI — 300 MB ham kayıt 0,17 sn'de taranıyordu ama bunu yapmak için `.jsonl` greplemeyi bilmek gerekiyordu. Arşivin değeri saklamada değil geri çağırmada: `/root/bin/ara` üç katmanı (kurate defterler → oturum özetleri → ham kayıt) tek komutta tarar ve nerede bulduğunu söyler.

---
*Kaynak: oturum özetleyicisi ölü bulundu 2026-08-18 → auto_session_save.py + .env GEMINI_MODEL + /root/bin/ara + /root/bin/hafiza-yayinla*
