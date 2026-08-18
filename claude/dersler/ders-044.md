---
ureten: hafiza-yayinla
tip: ders
no: 44
etiketler: [ders, rulebook]
---

# Ders 44 — Bir servis "çalışmıyor"ken önce SABİT model/sürüm adını sorgula — sağlayıcı eski modeli 503/404'e düşürmüş olabilir; faturalı hesap bile model kapasitesini aşamaz.

**Bir servis "çalışmıyor"ken önce SABİT model/sürüm adını sorgula — sağlayıcı eski modeli 503/404'e düşürmüş olabilir; faturalı hesap bile model kapasitesini aşamaz.** Fiş OCR çöktü; faturalı Gemini key sağlamdı (bakiye var) ama vision-gateway `gemini-3.5-flash`'a sabitti ve Google o modeli 503 ("high demand") veriyordu (paid tier bile — 503 model-seviyesi, key-seviyesi değil). `gemini-flash-latest` çalışıyordu, `gemini-2.0-flash` 404'e düşmüştü (kaldırılmış). İKİNCİ tuzak: yeni modele geçince config uyumsuzluğu (thinking_budget=0 → 3.5-flash kabul, flash-latest 400 INVALID_ARGUMENT reddeder). Kural: model 503/400 veriyorsa (a) `*-latest` alias'ı dene (sağlayıcı çalışan sürüme yönlendirir), (b) model-spesifik config'i (thinking/system_instruction) yeni modelde tek tek doğrula, (c) hata mesajını "servis" vs "girdi" diye ayır — yoksa kullanıcı foto/girdi suçlar (yanlış yön). Ayrıca: fallback zinciri (GLM/z.ai) öldüyse tek nokta = birincil; birincil model adı tek arıza noktası olmasın.

---
*Kaynak: fiş OCR gemini-3.5-flash 503 2026-07-24 → pool.FLASH_MODEL=flash-latest + _gen_cfg latest-guard + gider_foto servis_hatasi*
