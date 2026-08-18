---
ureten: hafiza-yayinla
tip: ders
no: 89
etiketler: [ders, rulebook]
---

# Ders 89 — Bir aracın hedef ADRESİ sabitse, dış dünya o adı değiştirdiği gün araç sessizce ölür — ve "başarısız" değil "eski cevap" döndürür.

**Bir aracın hedef ADRESİ sabitse, dış dünya o adı değiştirdiği gün araç sessizce ölür — ve "başarısız" değil "eski cevap" döndürür.** ccoto'nun telefon araçlarının hepsinde `adb -s 127.0.0.1:5555` sabitti. Telefon adb'ye yeniden bağlanınca cihaz **`emulator-5554`** adıyla listelendi (5554/5555 emülatör port çifti sayıldığı için ad değişir); sabit hedef `device not found` verdi, komut hiç koşmadı, **RC=0** döndü. `telss` görüntüyü yazamadı ama eski `~/_telss.png` dosyasını SİLMEDEN çektiği için **4 saat önceki ekranı "şu anki ekran" diye sundu** — ve ben o bayat görüntüyü okuyup ekranda olmayan bir şey hakkında karar vermeye başladım. Bayatlığı yakalayan şey ikinci bağımsız kaynaktı: görüntüdeki saat 02:38, telefonun saati 06:44 (#76'nın birebir tekrarı, bu kez saat damgası dedektör oldu). İkinci zarar: `tel -c` aynı sabit adı aradığı için "adb bağlanamadı → kablosuz hata ayıklama kapanmış" diye **yanlış teşhis** basıyordu; kullanıcı telefon ayarlarında olmayan bir arızayı arayacaktı. **Kural: dış dünyadaki bir kimliği (cihaz serisi, port, konteyner adı, oturum id) koda sabitleme — çalışma anında ÇÖZ; çözemezsen sus değil BAĞIR. Ve bir aracın ürettiği dosyayı okumadan önce SİL (varlığı değil tazeliği ölç).** Kapı deseni kilitler, sayıyı değil: hiçbir araçta sabit hedef olmayacak + hedef çözücü GERÇEKTEN var olacak (yoksa "sabiti silip yerine hiçbir şey koymamak" testi geçerdi) + görüntü yazımından önce silinecek.

---
*Kaynak: ccoto telefon araçları 4 saat bayat ekran gösterdi 2026-08-18 → tel_ortak.TEL_ADB_UZAK + tel_uzak._adb_hedef + telss rm-önce + tel -c gerçek seri + tests/test_adb_hedef.sh (9)*
