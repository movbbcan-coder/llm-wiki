---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

## 2026-10-23 — Tek seferlik duyurular + Telegram tam metin (Codex; canlı)

Sahip Codex. Kullanıcı genel duyuruların kaçırılmamasını, ders dışı olanların
bir kere bildirilmesini istedi. Gösterilen duyuru canlı DOM'dan doğrulandı:
26–30 Ekim Ayazağa–Maslak derslerinin çevrim içi yapılması; kullanıcıya kişisel
uygunluk çıkarılmadı. Genel Duyurular → Tüm Duyurular listesi ve detay şeması
normal menüyle doğrulandı. Öğretim elemanı mesajları açılmadı; genel Göster
işlemi site davranışı olarak okundu işaretleyebilir, okunma durumu dedup için
kullanılmaz. Snapshot kimlik/başlık/tarih/metin saklar; gönderen ve gizli alan yok.

`announcements.py` saf parser/kimlik/kural, `resources` gözlenen tek yeni kaynak,
`reader` arşiv/detay okuması, `store` ilk güncel duyuru yakalama, V2 kalıcı olay
ve Telegram kart/detay sayfaları eklendi. Yeni servis/zamanlayıcı yok. Ayarlar
→ Duyurular'da özet ve tam metin okunur; normal akademik ekranlarda web URL0.
Genel duyuru bir kez; sıra, okunma veya arşivden geri gelme tekrar üretmez.
Akademik gerçek içerik değişikliği yeni sürüm olabilir. İlk arşiv son7 gün/
yakın gelecekte açık akademik tarih ile daraltılır; eski arşiv topluca gönderilmez.
Kaynak cümlesi seçilir, yer/tarih/kişisel uygunluk uydurulmaz. Ek dosya açılmaz.

Canlı9 metin6,72s'de OK/live; Notlar→Duyurular tekrarı6,35s. HTTP yanıtı/iframe
DOM yarışı frame navigation olayıyla düzeltildi. İlk dağıtımdan sonraki taramada
geçici navigation Timeout gözlendi; aynı sırada tekrar edilemedi. Yanlış güncel
bildirim verilmedi. Bekleyen doğrulanmış bilgi taramadan önce gönderilir;
yalnız pending duyuru ağ hatasında mevcut işçi90sn arayla sınırlı tekrar yapar,
3 hatada durur. Auth/403/429/VNC/form korumaları aşılmaz. Arşiv45sn/3 sayfa
sınırını aşarsa kısmi başarı kabul edilmez; eski veri korunur.

Test493→511/511 (18 yeni),16,88s,6 eski uyarı; ağ kapalı/root salt okunur.
İki eski testin sabit kaynak/rota sayıları doğrulanmış yeni kaynak için uyarlandı.
Özel kod+DB yedeğiyle aynı bot güncellendi; son yedek
`veri/universite/releases/smart-ui-v2-20261023T153719Z`. Bot1271255 active,
NRestarts0; browser1171881/VNC594899 değişmedi. Son9 satır OK/live, bot kimliği
ve başlangıcı doğrulandı.2 güncel akademik duyuru tek728 karakter bildirimde
SENT; iki olay delivered, eski pending0. Yapay test mesajı yok.

Tam kanıt/sınırlar/geri dönüş: `.work-smart-ui-v2.bbDCir/docs/ANNOUNCEMENTS_DEPLOYED.md`.
Normal saatlik08–22 kontrol ve açık oturum şartı geçerlidir; fiziksel telefonda
tüm detay sayfalarının görsel kabulü yapılmadı. Yeni duyuru kaynağı artık canlıdır.
