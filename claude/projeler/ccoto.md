---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, ccoto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

## 🟢 YENİ OTURUM — BURADAN BAŞLA (son güncelleme 2026-08-18)

**Ne bu:** telefonu (Galaxy S24, Termux + ters SSH tüneli) Claude'un sürebildiği bir köprü +
telefondan Claude'u yönetebildiğin bir Android uygulaması. Amaç: kullanıcı telefona
dokunmadan iş yaptırabilsin ve izin isteklerini telefondan cevaplayabilsin.

**Durum: FAZ 0-4 bitti.** Kullanıcının canlı kullanım sonrası bildirdiği 6 maddenin 5'i de
bitti. Kalan tek iş aşağıda.

| Katman | Nerede |
|--------|--------|
| Telefon araçları | `/root/bin/` → `tel` · `otogor` · `otodokun` · `telss` · `telvid` · `telmod` · `tel_uzak.sh` (telefonda koşan TEK motor) |
| Köprü (VPS) | `/root/ccoto/backend/` → pm2: `ccoto-api` (127.0.0.1:8787) + `ccoto-bot` (@Ccotobot) |
| Dışa açılım | `https://ccoto.movbbcan.com` (Cloudflare → nginx → 8787), sır başlığı `X-Ccoto-Anahtar` |
| APK | `/root/ccoto/apk/` → derleme `apk/derle.sh` (uzak kutu tm-vpn-1), kurulum+kapı `apk/kur_ve_dogrula.sh` |
| Kapılar | `bash tests/tumu.sh` → **86 test yeşil** + `test_adb_hedef.sh` (python + zincir + mutasyon) · `tests/test_f20_kapi.sh` (10 uç kapısı) |
| Kanıtlar | `bulgular/` (ekran görüntüleri + faz kanıt dosyaları) |

**İlk 30 saniyede bilmen gerekenler (hepsi acı deneyimle öğrenildi):**
1. **Tünel kopuk olabilir** — `tel -c` ile bak. Kopuksa telefonda Termux'ta tek komut
   gerekir (kullanıcı çalıştırmalı); VPS'ten onarılamaz. Nöbetçi haber verir ama artan
   aralıkla (30 dk → 2 sa → 8 sa → günde bir), susturma: `veri/tunel_sessiz` dosyası.
2. **Telefon kilitliyse** ekran okunamaz, düğmeye basılamaz — `dumpsys` boş döner.
3. **APK kurulumu sessizce kopabilir** (scp) — `kur_ve_dogrula.sh` artık md5 karşılaştırıyor;
   çıktısını `grep`'ten geçirip verdictini KAYBETME (bir kez 40 dakika kaybettirdi).
4. **`telmod ac`** telefonu sürerken ŞART (çağrı hook'ları uygulamayı deviriyor), iş bitince
   `telmod kapa` — script'lerde `trap EXIT` ile garanti.
5. **`screencap` overlay'i görmez** → baloncuğu görmek için `telvid` (screenrecord yolu).
6. **Canlı Claude TUI'sinde metinle dokunma çalışmaz** (uiautomator dump alınamaz) →
   `otodokun -k X,Y` koordinat yolu.

**⚠ 2026-08-18 — ÖLÇÜLMÜŞ ARIZA VE DÜZELTMESİ (araçlar sessizce ölmüştü):**
Telefon adb'ye yeniden bağlanınca cihaz `127.0.0.1:5555` yerine **`emulator-5554`** adıyla
listelendi. Tüm araçlardaki sabit `-s 127.0.0.1:5555` "device not found" verdi; komut hiç
koşmadı ama **RC=0** döndü ve `telss` silinmemiş eski PNG'yi "şu anki ekran" diye sundu
(4 saat bayat görüntü okundu). `tel -c` de "adb bağlanamadı" diyordu — yanlış teşhis
("kablosuz hata ayıklama kapanmış") üretiyordu. Fix: hedef ÇALIŞMA ANINDA çözülüyor
(`tel_ortak.sh` → `TEL_ADB_UZAK` SSOT + `tel_uzak.sh` → `_adb_hedef`), görüntü yazımından
önce hem uzak hem yerel kopya siliniyor, `tel -c` gerçek seriyi yazıyor.
Kapı: `tests/test_adb_hedef.sh` (9 kontrol, mutasyonla doğrulandı — sabit hedef geri konunca
kırmızıya dönüyor). Rulebook #76'nın ikinci kurbanı.

**KALAN TEK İŞ (madde 5):** `otogor` "bu bir web sayfası" desin — ön plan tarayıcı ve öğe
listesi sayfa düğümü içermiyorsa "koordinat moduna geç" uyarısı versin; ajan bunu bir dokunma
harcayarak keşfetmesin. Telefon bağlıyken ve tarayıcı açıkken yapılacak.

**Sonraki adım adayları:** FAZ 4(c)'nin "işle" adımı — Harem turundan çıkan tek gerçek aday
**takip listesi**'ni denk'e eklemek (şartı: net varlığa KARIŞMAMALI). Detay:
`bulgular/faz4-harem-envanter.md` + artifact: https://claude.ai/code/artifact/8df7ea85-e99c-4858-bde9-ff28334a8cb8

**Bu işten çıkan rulebook dersleri:** #78 (terminal protokolü/scroll) · #79 (OS özelliği tüm
önkoşullar sağlandığı hâlde çalışmıyorsa cihaz genelini ölç, OEM karşılığını ara) · #80 (bir
kanalın koptuğunu haber veren mesaj o kanala emanet edilemez) · #81 (deseni tek örnekten
genelleme; tanımayı gevşek/sıkı iki katmana ayır) · #82 (uyarının tekrarı da bilgi taşımalı).

---


*Başlangıç: 2026-08-12 · Ad alanı: **CCOTO FAZ 0-4** · Oturum: `ccoto`*
