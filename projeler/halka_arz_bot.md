# halka_arz_bot

- **Domain:** bireysel
- **Durum:** aktif
- **Bekleyen görev:** 1
- **Ajanlar:** bildirim, cikis_stratejisi, kap_finansal, lot_tahmini, analiz, sheets_agent, tarama, simulasyon
- **Son güncelleme:** 2026-04-11 07:00

## Tahta

# halka_arz_bot — Proje Tahtası
> 🏷 Durum: aktif

## 🎯 VİZYON & MASTER PROMPT

Borsa İstanbul halka arz (IPO) takip ve analiz sistemi. KAP.org.tr ve BIST'i otomatik izleyerek
yeni IPO'ları tespit eder; izahname PDF'ini okuyarak temel finansal analiz yapar; çoklu hesap
(aile/arkadaş) simülasyonu ile 1-5 hesap senaryosunda kazanç/bloke para/verimlilik tablosu üretir;
tarihsel veriye dayalı çıkış stratejisi önerir; Telegram üzerinden bildirir.

**Hedef:** Profesyonel bir yatırımcının 3 saatte yapacağı IPO araştırmasını 3 dakikada otomatik yap.
**Karar insanda kalır, bot veriyi hazırlar.**

---

## ✨ OLGUNLAŞTIRILMIŞ VİZYON

Halka arz yatırımcısının tüm araştırma sürecini otomatize eden, 6 modüllü otonom bir analiz sistemi:

1. **Tarama**: KAP + BIST günlük tarama → yeni IPO tespiti
2. **Analiz**: İzahname PDF parse → bilanço + değerleme + güç skoru (0-100)
3. **Lot Tahmini**: Talep yoğunluğu modeli → kişi başı lot tahmini
4. **Çoklu Hesap Sim**: 1-5 hesap senaryosu → kazanç/bloke/verimlilik tablosu
5. **Çıkış Stratejisi**: Tarihsel tavan verisi → "X. tavanda sat" önerisi
6. **Bildirim**: Telegram → anında haber + özet rapor

---

## 🤖 AJAN MİMARİSİ

- **tarama_ajan** (agents/tarama.py)
  Rol: KAP.org.tr ve BIST'i scrape eder, yeni IPO duyurularını yakalar
  Görev sınırı: Sadece veri toplar, analiz yapmaz
  Tetikleyici: Her gün 08:00 + anlık kontrol

- **analiz_ajan** (agents/analiz.py)
  Rol: İzahname PDF indir, bilanço parse et, finansal oranları hesapla, güç skoru üret
  Görev
