---
ureten: hafiza-yayinla
tip: ders
no: 43
etiketler: [ders, rulebook]
---

# Ders 43 — İki koruma birbirine "öteki hallediyor" diye güvenirse ve biri sessizce çalışmıyorsa, harcama ikisinin arasından düşer.

**İki koruma birbirine "öteki hallediyor" diye güvenirse ve biri sessizce çalışmıyorsa, harcama ikisinin arasından düşer.** Garanti kart harcaması: `get_dashboard_data` fişi düşmüyor ("bildirim zaten düşürür" varsayımı) ama `bildirim_parser` POS-slip formatını ("...dijital slibi oluşturulmuştur") tanımıyordu → `parse()` None → bildirim de düşmüyordu. Sonuç: 276,75 ₺ ne bildirimle ne fişle düştü, sessizce kayboldu, bakiye şişik kaldı. MacroDroid suçlanıyordu ama o okumuştu (ham.jsonl'da vardı) — hata parser'ın tanımadığı formattaydı. Kural: "A, B'yi düşürür" varsayımı A'nın GERÇEKTEN düşürdüğünü ölçmeden kurulamaz; bir kaynağın "bunu öteki halleder" mantığı, ötekinin o girdiyi işlediğini kanıtlamalı. Yeni bir bildirim formatı gelince parser'ın tanıyıp tanımadığını ham.jsonl'dan doğrula (tanınmayan → ham log'da None olarak kalır, sessizdir).

---
*Kaynak: Garanti kart harcaması 276,75 düşmedi 2026-07-24 → bildirim_parser._GARANTI_KART + test*
