---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

## 2026-09-30 — 🟡 PARK: Chess.com Satranç Antrenörü

**Tek hedef:** CCOTO baloncuğundan, yalnız Chess.com'un izinli eğitim bağlamlarında
(bot, bulmaca, analiz ve Classroom) mevcut konumu okuyup Türkçe kademeli ipucu vermek.
Canlı insan oyununda (dereceli veya gündelik) dış yardım Chess.com kuralına aykırı;
bu ekranlarda analiz özelliği fail-closed olacak. Kardeşle ortak yardımlı çalışma
için Chess.com Classroom kullanılacak; resmi dokümana göre Basic hesap bir katılımcı
alabiliyor ve değerlendirme/motor çizgilerini destekliyor.

**Ölçüm:** `ccoto-api` ve `ccoto-bot` online (8 gün, restart 0), telefon yardımcısı
bağlı. SSH/ADB tüneli kapalı; ilk erişilebilirlik ağacı okuması için zorunlu değil.
VPS'te OpenCV/Pillow var; `python-chess` ve Stockfish yok. Mevcut hizmet yalnız metin
ağacını okuyor, grafik tahtanın konuma dönüşümü henüz yok.

**BİTTİ tanımı:** Gerçek telefonda Chess.com bot konumunu doğru FEN'e çevirir,
kademeli Türkçe ipucu verir ve canlı insan oyunu ekranında analizi reddeder. Üç sabit
konum + bir gerçek cihaz akışıyla doğrulanır.

**Sıradaki adım:** Kullanıcı Chess.com → Botlarla Oyna ekranında bir oyunu açıp
`hazır` diyecek; `ccoto gor` ile tahta düğümlerinin erişilebilirlikte görünüp
görünmediği salt-okur ölçülecek. Sonuca göre metin ağacı veya ekran görüntüsü
yolu seçilecek; ölçmeden tanıma kodu yazılmayacak.

**Canlı P0 sonucu:** Ön plan paketi `com.chess` olarak doğrulandı. Bot ekranındaki
`Geri Al`, `İpucu`, `Terk Et`, son hamle metinleri ve koordinatlar erişilebilirlikte
okundu; tahta kareleri ve taşlar hiç dönmedi. Yalnız hamle satırına dayanmak eksik
geçmişte yanlış konum üretebilir. Sonraki kapı: Termux ters SSH/ADB tüneli açılıp
aynı bot konumunun ekran görüntüsü alınacak; Android erişilebilirlik servisinin
`takeScreenshot` yolu için resmi API'nin istediği `canTakeScreenshot` yeteneği doğrulandı.

**2026-09-30 uygulama durumu:** Neo taş şablonlarıyla gerçek 1080×2340 Chess.com
görüntüsündeki 64 kare okundu; yerleşim
`r1b1k1nr/pppp1ppp/5q2/2P5/4P1n1/2N2Q2/PPP2PPP/R1B1KB1R`, yön `siyah`,
en yüksek hata `10,21`, en düşük rakip farkı `7,52`. Yeni oyun başlangıcından
en fazla iki yarım hamlelik tek yasal zincir izleniyor; belirsizlikte oturum sıfırlanıyor.
Stockfish 16 yerel kuruldu; API yalnız `com.chess` + `Geri Al/İpucu/Terk Et` bot
bağlamını kabul ediyor. Baloncukta `fikir/kare/hamle` düğmeleri ve Android
`takeScreenshot` komutu derlendi. Python `138/138`, canlı API `18/18`, APK derleme
yeşil; APK SHA-256 `eb6a073799d9…`. `ccoto-api` proje `.venv` yorumlayıcısıyla
online ve PM2 kaydedildi. APK aktarımında telefon `sshd` CLOSE-WAIT'e düştü;
kurulum yapılmadı. **PARK koşulu:** kullanıcı Termux ters tünelini yeniden kurar,
ardından `kur_ve_dogrula.sh` ve yeni bot oyunu gerçek cihaz kabul testi tamamlanır.
