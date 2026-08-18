---
ureten: hafiza-yayinla
tip: ders
no: 82
etiketler: [ders, rulebook]
---

# Ders 82 — Bir uyarının DOĞRU olması yetmez — TEKRARI da bilgi taşımalı; taşımıyorsa uyarı sistemi kendini yok eder.

**Bir uyarının DOĞRU olması yetmez — TEKRARI da bilgi taşımalı; taşımıyorsa uyarı sistemi kendini yok eder.** ccoto'nun tünel nöbetçisi (rulebook #80) arıza sürerken **30 dakikada bir** aynı mesajı gönderiyordu. Teknik olarak kusursuzdu: durum diskte, soğuma çalışıyor, iki kanaldan gidiyor. Ama kullanıcı iki gün boyunca onlarca bildirim aldı ve *"rahatsız ediyor"* dedi — ki bunun doğal sonucu tüm ccoto bildirimlerine bakmayı bırakmaktır; yani **gerçek bir izin isteği geldiğinde de görmeyecekti** (#32'nin tam tersinden gelen hâli: koruma, kendi kanalını çöpe çevirerek susturucuya dönüşür). Kural: bir durum bildirimi tekrar edecekse **aralık artmalı** (30 dk → 2 sa → 8 sa → günde bir) ve durum değişince sayaç SIFIRLANMALI — yoksa ya yeni arıza geç haber verilir ya eskisi bunaltır. Ayrıca kullanıcıya **açık bir susturma yolu** bırak (`veri/tunel_sessiz` dosyası): susturma körleşme DEĞİLDİR — nöbetçi durumu izlemeye devam eder, yalnız konuşmaz. Genel biçim: "haklı olmak" ile "işe yaramak" ayrı şeylerdir; bir uyarı, alıcısının davranışını iyileştirmiyorsa tasarımı yanlıştır.

---
*Kaynak: ccoto tünel bildirimi bunaltması 2026-08-16 → tunel.SOGUMA_ADIMLARI + SESSIZ_DOSYA + test_tunel.py (16)*
