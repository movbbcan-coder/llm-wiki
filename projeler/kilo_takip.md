# kilo_takip

- **Domain:** bireysel
- **Durum:** tahta yok
- **Bekleyen görev:** 0
- **Ajanlar:** analysis_agent, tracker_agent, hunger_agent, photo_agent, workout_agent, profile_agent, fitness_agent, hydration_agent, motivation_agent
- **Son güncelleme:** 2026-04-11 07:00

## Tahta

# TAHTA — Kilo Takip AI Asistanı
> Domain: BİREYSEL (Gizli)
> Oluşturulma: 2026-04-06
> Son güncelleme: 2026-04-06

---

## 🎯 VİZYON

Günlük kullanım için kişisel AI kilo takip asistanı. Yemek kaydı, kilo takibi, ilerleme analizi ve motivasyon desteğini tek Telegram botunda birleştirir. Tıbbi tavsiye vermez — sürdürülebilir ve dengeli kilo kaybını hedefler.

---

## 🤖 AJAN MİMARİSİ

| Ajan | Dosya | Görev |
|------|-------|-------|
| `tracker_agent` | `agents/tracker_agent.py` | Yemek ve kilo kaydı alma, Google Sheets'e yazma |
| `analysis_agent` | `agents/analysis_agent.py` | İlerleme analizi, trend hesaplama, özet rapor |
| `motivation_agent` | `agents/motivation_agent.py` | Tutarlılık takibi, hatırlatma, pozitif geri bildirim |

---

## 📑 VERİ YAPISI (Google Sheets)

| Tablo | Sütunlar |
|-------|----------|
| KILO_LOG | Tarih, Kilo (kg), Not |
| YEMEK_LOG | Tarih, Öğün, Yemek, Kalori (tahmini), Not |
| HEDEF | Başlangıç Kilo, Hedef Kilo, Başlangıç Tarihi, Hedef Tarihi |

---

## ⚙️ GÜVENLİK KURALLARI

- Tıbbi teşhis YASAK
- Aşırı diyet tavsiyesi YASAK
- Güvensiz kalori kısıtlaması YASAK
- Her zaman dengeli ve sürdürülebilir yaklaşım

---

## 🚀 FAZ PLANI

### Faz 1 — İskelet [3 gün] ✅ TAMAMLANDI
- [x] Proje dizin yapısını kur (`agents/`, `core/`)
- [x] `.env.example` ve `config.py` yapısını kur
- [x] `core/sheets.py` — tüm CRUD fonksiyonları yazıldı (OAuth ile)
- [x] `.env` oluşturuldu (TELEGRAM_BOT_TOKEN + SPREADSHEET_ID)
- [x] Google Sheets bağlantısı test edildi — OK (`
