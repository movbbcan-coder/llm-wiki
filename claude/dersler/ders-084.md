---
ureten: hafiza-yayinla
tip: ders
no: 84
etiketler: [ders, rulebook]
---

# Ders 84 — Bir kanal sessizce ölebiliyorsa er ya da geç ölür ve haftalarca fark edilmez — her giriş kanalının "sustum" nöbetçisi olmalı.

**Bir kanal sessizce ölebiliyorsa er ya da geç ölür ve haftalarca fark edilmez — her giriş kanalının "sustum" nöbetçisi olmalı.** MacroDroid→VPS banka bildirim hattı 5 Ağustos'ta sustu, **10 gün** kimse görmedi; o süre boyunca gelen havale · kart harcaması · virman tespiti · kumbara varışı KÖR kaldı. Ortaya çıkışı tesadüfî: kullanıcı "805 ₺ yatırdım ama ekran değişmedi" dedi. Sunucu ucu sağlamdı (elle test: yerel 200, nginx+HTTPS 200, kayıt düştü) → arıza telefon tarafındaydı. Yani kusur hattın kopması değil, **kopmayı kimsenin haber vermemesiydi** (#80'in birebir tekrarı, bu kez giriş yönünde). Fix: `trading/bildirim_nobetci.py` — eşik VERİDEN ölçüldü (78 gerçek bildirimin boşluk dağılımı: medyan 2,0 sa · %90 22,5 sa · gözlenen en uzun MEŞRU sessizlik 51,9 sa → eşik 60 sa; uydurulmuş 24 sa yanlış alarm üretir, güveni aşındırırdı). Üç incelik teste bağlandı: (a) elle atılan hat testi (`app=TEST*`) hattı CANLI göstermemeli — yoksa nöbetçi kendi testiyle susturulur; (b) "hiç kayıt yok / okuyamıyorum" ayrı bir ALARM hâlidir (#35); (c) soğuma sentinel'i `None`, `0.0` değil ve soğuma yalnız mesaj GERÇEKTEN gidince başlar (#80). **İKİNCİ DERS, aynı turda ve utandırıcı:** çift sayımı önleyen kapıyı yazarken ekstre dosyasının anahtarını ÖLÇMEDEN `islemler` diye uydurdum (gerçeği `kayitlar`) → kapı sessizce boş liste alıp `False` döndü ve 1.065 ₺ deftere ikinci kez yazıldı; canlı çıktıyı okuyunca (`ekstrede: false`) yakalandı. **Yanlış alan adı = sessiz kapalı kapı**; şema testle kilitlenmeli (`assertIn("kayitlar", ...)`) ve kapının canlı yükleyicisi ayrıca "damga üretiyor mu" diye sınanmalı — saf çekirdek testleri geçerken yükleyici kör olabilir.

---
*Kaynak: bildirim hattı 10 gün ölü + kumbara çift sayımı 2026-08-16 → trading/bildirim_nobetci.py + bot.py saatlik tik + kumbara_yatirim.ekstrede_zaten_var + test_bildirim_nobetci.py (16) + test_kumbara_yatirim +8*
