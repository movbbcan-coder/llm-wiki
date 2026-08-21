---
ureten: hafiza-yayinla
tip: ders
no: 94
etiketler: [ders, rulebook]
---

# Ders 94 — `set -o pipefail` + `grep -q` = SESSİZCE AÇILAN KAPI.

**`set -o pipefail` + `grep -q` = SESSİZCE AÇILAN KAPI.** `ccsil`'in "bu yol canlı bir PM2 servisinin dizini mi" koruması ilk testte tetiklenmedi: `pm2 jlist \| ... \| grep -q HIT` — `grep -q` ilk eşleşmede çıkıyor, yukarı akıştaki `pm2`/`cut` SIGPIPE alıp 141 dönüyor, `pipefail` bunu pipeline hatası sayıyor → fonksiyon "canlı değil" diyor. Yani koruma **eşleşme BULDUĞU için** başarısız oluyordu; hiç eşleşme olmasa doğru cevap verecekti. Canlı `/root/banka/bank_app` "taşınabilir" göründü. Fix: `grep -q` yerine çıktıyı değişkene al (`vur=$(...)`; `[[ -n $vur ]]`). **Kural: guard'ı yazdıktan sonra POZİTİF vakayla test et (gerçekten reddediyor mu) VE negatif vakayla (meşru hedefi hâlâ geçiriyor mu) — ikincisi olmadan düzeltme kapıyı susturucuya çevirebilir.** (#32/#35 ailesi: susan koruyucu, olmayandan beter.)

---
*Kaynak: ccsil PM2 kapısı 2026-08-21 → /root/bin/ccsil pm2_canli_mi*
