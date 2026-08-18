---
ureten: hafiza-yayinla
tip: ders
no: 26
etiketler: [ders, rulebook]
---

# Ders 26 — OAuth refresh token'ları **ROTATE** eder: bir kez kullanınca eskisi GEÇERSİZ olu

OAuth refresh token'ları **ROTATE** eder: bir kez kullanınca eskisi GEÇERSİZ olur, yanıtta yeni refresh_token döner. Refresh'i ASLA "kaydetmeden test etme" → eski token ölür, hesap kırılır (yeniden login şart). Claude OAuth refresh: `POST https://api.anthropic.com/v1/oauth/token` (console.* = 404), **User-Agent zorunlu** (yoksa Cloudflare 1010), body `{grant_type:refresh_token, refresh_token, client_id:9d1c250a-...}`. Yanıtı (access+refresh+expiresAt) ATOMİK yaz, sadece PASİF profile dokun (aktif hesabı claude yönetir, dokunma)

---
*Kaynak: claude2 profil2 token'ı test sırasında kırıldı 2026-06-18 → usage-fetch.sh güvenli refresh*
