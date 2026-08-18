---
ureten: hafiza-yayinla
tip: ders
no: 64
etiketler: [ders, rulebook]
---

# Ders 64 — İki otomasyon aynı tekil kaynağı (ekran, port, dosya) kullanıyorsa hangisinin öncelikli olduğu AÇIKÇA söylenmeli — yoksa yardımcı olan, yardım ettiği işi bozar.

**İki otomasyon aynı tekil kaynağı (ekran, port, dosya) kullanıyorsa hangisinin öncelikli olduğu AÇIKÇA söylenmeli — yoksa yardımcı olan, yardım ettiği işi bozar.** Claude adb ile uygulamayı sürerken dokunuşlar sürekli Termux'a gidiyordu, bir kez klavye bile açtı. Suçlu sanılan MacroDroid değil, **bizim kendi çağrı sistemimizdi**: izin isteği → `izin-bildirim.sh` ntfy push → MacroDroid Termux'u öne getirir → izin verilir → `geri-don.sh` "önceki uygulamaya dön" der → ama önceki uygulama artık TERMUX'tur. Yani otomasyona yardım etsin diye kurulmuş bildirim zinciri, otomasyonu deviriyordu. Çözüm bayrak: `telmod ac/kapa` → üç hook da susar. **DİKKAT: susturma da bir kilittir** — iş bitince `telmod kapa` denmezse kullanıcının telefonu bir daha hiç çağrılmaz (#32 ailesi: sessiz kilit). ÜÇÜNCÜ ders: teşhis için iz şart — `/tmp/claude-cagri.log` olmasa suçlu üç tur boyunca tahmin edilecekti.

---
*Kaynak: Denk cihaz otomasyonu 2026-08-09 → telmod + stop-termux-cagir/geri-don/izin-bildirim kapıları*
