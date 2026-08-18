---
ureten: hafiza-yayinla
tip: ders
no: 83
etiketler: [ders, rulebook]
---

# Ders 83 — Bir kaydı "yok" ilan etmeden önce ARADIĞIN ALANIN dolu geldiğini doğrula — sağlayıcı alanı maskeleyebilir ve yokluk kanıtı sahte çıkar.

**Bir kaydı "yok" ilan etmeden önce ARADIĞIN ALANIN dolu geldiğini doğrula — sağlayıcı alanı maskeleyebilir ve yokluk kanıtı sahte çıkar.** P2P'de "ilanımız piyasa listesinde görünmüyor, satış yapamamanın asıl sebebi bu" diye EN YÜKSEK öncelikli bir arıza kaydedildi (105 ilan tarandı, bizimki yok). Gündüz ölçümünde ilan **95/105. sıradaydı, listede duruyordu**: `item/online` yanıtı `accountId` alanını TÜM ilanlar için `"0"` (maskeli) döndürüyor, kimlik kıyası `accountId == kendi_id` olduğu için hiçbir zaman tutmuyordu. Kimlik gerçekte `nickName`'de. Aynı bozuk kıyas ÜRETİMDE de vardı (`get_dashboard_data` `sen` bayrağı → dashboard kendi ilanımızı hiç vurgulamıyordu) ve `piyasa_konumu` bulamayınca sırayı SESSİZCE fiyattan tahmin ediyordu — yani gerçekten piyasadan düştüğümüz gün ekran aynı sayıyı gösterecekti (#35: denetleyemediğim hâl ayrı bir bulgu olmalı; artık `sen_listede` + "(tahmini)" etiketi). İKİNCİ tuzak aynı yerde: liste tek sayfada 100 ile kesiliyordu, piyasa 106'ya çıkmıştı ve biz pahalı uçtayız (fiyat artan sıralamada 95.) → sayfalama eklenmeseydi ilan gerçekten listeden düşecek ve yanılgı KENDİNİ doğrulayacaktı. **Kural: "X listede yok" hükmünden önce (a) eşleştirme alanının canlı örnekte dolu olduğunu, (b) listenin tamamının çekildiğini ölç; ikisi de yoksa bulgu "bilinmiyor"dur, "yok" değil.** YAN DERS: yanlış alarm bir geceyi yaktı — teşhis scripti tek satırlık bir alan varsayımına dayanıyordu ve kimse alanı basıp bakmamıştı (ham yanıtı bir kez yazdırmak yeterdi).

---
*Kaynak: P2P ilan görünürlüğü sahte alarmı 2026-08-15 → bybit_isler.p2p_nick + sayfalama · ilan_durum.kendi_mi + sen_listede · get_dashboard_data · test_ilan_durum +7 · test_ilan_karti_zinciri +2*
