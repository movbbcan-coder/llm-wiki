---
ureten: hafiza-yayinla
tip: ders
no: 69
etiketler: [ders, rulebook]
---

# Ders 69 — İzin kuralı yazmak ≠ onay sorulmaması: allow kuralı komut ÖNEKİNE bakar, sarmalayıcı/değişken ataması/boru onu bozar — ve her onay, cihaz otomasyonunu deviren bir ekran değişimidir.

**İzin kuralı yazmak ≠ onay sorulmaması: allow kuralı komut ÖNEKİNE bakar, sarmalayıcı/değişken ataması/boru onu bozar — ve her onay, cihaz otomasyonunu deviren bir ekran değişimidir.** Denk cihaz doğrulamasında `Bash(ssh -p 8022 -i ...:*)` allow'daydı ama benim komutlarım `SS=/tmp/...; ssh ... | base64 -d > f` ve `telui '...'` biçimindeydi → önek eşleşmedi → her adımda onay soruldu. Kullanıcı onay verebilmek için ekranı İKİYE BÖLDÜ; Termux odağı aldı ve `input tap`'lerim 40 dakika boyunca Denk'e değil kullanıcının terminaline gitti (uygulama açılmıyor sanıldı, üç yanlış hipotez kuruldu: split-screen, `--windowingMode`, divider sürükleme). Çözüm: (a) allow listesine SARMALAYICILARI da ekle (`Bash(tel:*)`, `Bash(telui:*)`), (b) o oturumda her adımı **tek, önekle eşleşen** komuta indir — yerel boru/değişken yerine ayrıştırmayı UZAK tarafa taşı (telefonda `ui.sh`, çıktı zaten sade), ekran görüntüsünü `ssh`+`adb pull` / `scp` ikilisiyle al (ikisi de allow'da). Ders #64'ün kardeşi: otomasyona yardım için kurulan şey (izin kapısı) otomasyonu deviriyor.

---
*Kaynak: Denk KARAR FAZ 0 cihaz doğrulaması 2026-08-09 → settings.json allow + denk/ss/ui_remote.sh*
