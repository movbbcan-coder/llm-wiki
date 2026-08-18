---
ureten: hafiza-yayinla
tip: ders
no: 81
etiketler: [ders, rulebook]
---

# Ders 81 — Bir deseni TEK örnekten genelleme — ve iki koruma üst üste binince gerçek isteği birlikte öldürebilir.

**Bir deseni TEK örnekten genelleme — ve iki koruma üst üste binince gerçek isteği birlikte öldürebilir.** ccoto'da Claude Code izin istemini tanıyan desenler F1.5'te tek bir canlı örnekten (`Do you want to allow Claude to fetch this content?`) kilitlenmişti; "fixture gerçek istemden alındı" diye güvenli sanıldı. Gerçek hayatta gelen istem `Do you want to create sheets_dogrula.py?` oldu → hiçbir desen tutmadı. Zincir: hayalet temizliği (ekranda istem yoksa kaydı DÜŞTÜ yap) isteği düşürdü → kullanıcı Telegram'da ✅'ye bastı → "bu istek zaten 'dustu'" → **gerçek görev yarıda kaldı ve kullanıcı sebebini bilemedi**. İki koruma da tek başına doğruydu; birlikte, çok dar bir öncüle (desen listesi tam) dayandıkları için gerçek isteği öldürdüler. **Kural: bir metin desenini kilitlerken örneğin KENDİSİNİ değil, o metnin DEĞİŞMEYEN İSKELETİNİ yakala** (burada: "Do you want to …?" sorusu + numaralı `1. Yes` seçenek bloğu). **İkinci kural — tanımayı iki katmana ayır:** "bu kayıt hâlâ canlı mı?" sorusu GEVŞEK olmalı (yanlış negatif gerçek isteği sessizce öldürür), "tuşa basayım mı?" sorusu SIKI (Enter geri alınamaz; yapısal kanıt şart). Tek eşikle ikisini birden karşılamaya çalışmak, ya sahte onay ya sessiz kayıp üretir.

---
*Kaynak: ccoto canlı izin arızası 2026-08-14 → istem.cevap_verilebilir_mi + kopru.izin_cevapla + fixtures/izin_istemi_dosya.txt*
