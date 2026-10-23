---
ureten: hafiza-yayinla
tip: proje
etiketler: [proje, oto]
---

# ccoto — Ajan Telefon Kontrolü + Chat APK (yaşayan defter)

## 2026-10-23 — Beykent V2 üretime alındı; Telegram içi kullanım (Codex)

Kullanıcı “Tamam uygula” diyerek üretim geçişini onayladı; web'e tekrar
yönlendiren bir arayüz istemedi. Sahip Codex. Mevcut kopyadaki `v2_ui.py`
etki analizi sonrası daraltıldı: dört akademik ekrandaki URL düğmeleri kaldırıldı,
resmî bağlantılar Ayarlar → Resmî kaynaklar altında isteğe bağlı kaldı.
Takvim metnindeki sabit09.00 yerine seçilen özet saati gösteriliyor.6 yeni
regresyon önce kırmızı, düzeltme sonrası479/479 geçti (15,40s,6 eski uyarı).

Başlangıç18 SHA ve boş eski bildirim kuyruğu tekrar doğrulandı. Kontrollü
tek seferlik geçiş betiği dry-run ardından çalıştırıldı: özel kod/SQLite yedeği
`veri/universite/releases/smart-ui-v2-20261023T131404Z` (700). Yalnız mevcut
bot servisi durdurulup5 Python dosyası güncellendi, V2 kapısı açıldı ve aynı
servis başlatıldı. Bot PID1203495→1228069 active/NRestarts0; browser1171881,
VNC594899 aynı PID ile active/NRestarts0. Yeni Telegram bağlantısı ve izinli bot
kimliği doğrulandı;5 canlı kod SHA çalışma kopyasıyla aynı. İkinci bot/zamanlayıcı
yok, .env/cookie/browser konfigürasyonu değişmedi.

Canlı read-only denetimde4/4 akademik kart0 web düğmesi ve4096 karakter altında.
Normal ilk kontrol AUTH_REQUIRED gördü ve1 gerçek oturum uyarısı SENT; yapay
test mesajı gönderilmedi. Kullanıcı girişini manuel yenilemeli; eski kayıtlar
güncelmiş gibi gösterilmiyor. Girişten sonraki günlük okuma/hatırlatma Telegram
içindedir. Günlük özet saati seçimi soruldu; henüz yanıt yok, saat varsayılmadı.
Botta Ayarlar → Özet saati seçilene kadar yeni ders özeti başlamaz; mevcut
takvim hatırlatmaları korunur. Telefon üzerinde görsel kabul yapılmadı.

Güncel kanıt ve açık sınırlar: `.work-smart-ui-v2.bbDCir/docs/DEPLOYED.md`,
`docs/LIVE_AUDIT.json`. Önceki REPORT/RUNBOOK onay öncesi fotoğrafıdır;
üretime geçiş durumu bu yeni kayıtla tamamlandı.
