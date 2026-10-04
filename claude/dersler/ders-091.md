---
ureten: hafiza-yayinla
tip: ders
no: 91
etiketler: [ders, rulebook]
---

# Ders 91 — Bir nöbetçinin ÖLÇÜM aracı, izlediği olayın tetikleyicisiyle aynıysa nöbetçi kendi kendini besler — ve düzeltmenin ilk turu bunu görmez.

**Bir nöbetçinin ÖLÇÜM aracı, izlediği olayın tetikleyicisiyle aynıysa nöbetçi kendi kendini besler — ve düzeltmenin ilk turu bunu görmez.** #90'da tünel bildirimi "talep üzerine" moduna alındı: haber ancak bir araç (`tel`) tüneli kullanmaya çalışıp başarısız olunca gidecekti. Kullanıcı yine bildirim aldı — *"ben oto'yu kullanmıyorum, o zaman tünele bağlanmanın ne önemi var"*. Sebep: nöbetçinin sağlık ölçümü **`/root/bin/tel` çalıştırıyordu**; yeni eklenen `tel_ssh` kapısı bağlanamayınca "tünel lazım oldu" işaretini bırakıyor, nöbetçi bir sonraki turda o işareti görüp bildiriyordu. Yani ihtiyacı üreten şey, ihtiyacı bekleyen şeyin kendisiydi (canlı kanıt: `tunel_talep` damgası 27 sn önce, kaynak `tel`, kullanıcı telefona hiç dokunmamış). **Kural: bir koruyucu eklerken "bu işareti benim kendi ölçümüm de üretebilir mi?" diye sor; üretebiliyorsa ölçüm çağrısı iz bırakmayacak biçimde İŞARETLENMELİ** (`TEL_TALEP_YOK=1`) — ve bayrağa iki dil birden uymalı (Python geçirir, kabuk uyar; biri yok sayarsa döngü aynen sürer ve kimse fark etmez, #65/#84). **Daha iyisi: kökten kaldır** — kimse tüneli istemiyorken ölçüm de yapılmasın. Ölçüm yoksa tetikleme de yok, üstelik boşuna ssh denemesi de olmaz; kullanıcının sorusu zaten tasarımın cevabıydı. Kapı ölçümü SAYAR (`olcum_sayisi == 0`), etiketi değil: "boştayken konuşmadı" yetmez, "boştayken hiç bakmadı" da kanıtlanmalı. Bu, #84'ün ters yönü — orada elle atılan test hattı nöbetçiyi SUSTURUYORDU, burada nöbetçinin kendi ölçümü onu KONUŞTURUYOR.

---
*Kaynak: ccoto tünel bildirimi üçüncü tur 2026-08-21 → tunel._nobet_ic talep-yoksa-ölçüm-yok + saglik() TEL_TALEP_YOK + tel_ortak.tel_talep_isaretle bayrağı + test_tunel.py (24, üç mutasyonla)*
