---
ureten: hafiza-yayinla
tip: ders
no: 50
etiketler: [ders, rulebook]
---

# Ders 50 — Bir "verimlilik" aracı native araçları permission ile YASAKLAYIP kendi araçları kod tabanıyla uyumsuzsa, araç net negatiftir — zorunlu-modu kaldır, opt-in yap.

**Bir "verimlilik" aracı native araçları permission ile YASAKLAYIP kendi araçları kod tabanıyla uyumsuzsa, araç net negatiftir — zorunlu-modu kaldır, opt-in yap.** lean-ctx v6 kendini yükseltip `settings.json permissions.deny=[Read,Grep,Glob]` ekledi + shell-hook her komut çıktısını sarıp TÜRKÇE karakterde ('ş','ı') `char boundary` (dictionaries.rs:462) çöküyordu → oturum boyu `LEAN_CTX_DISABLED=1` zorunlu, sonunda MCP koptu (native yasak + ctx_* ölü = kilit). Türkçe kod tabanı + byte-offset truncation bug'ı = temelden uyumsuz. Fix: settings.json deny temizle + 9 lean-ctx hook kaldır + MCP kaydını sil + CLAUDE.md "native denied" bloğunu "native BİRİNCİL" yap + shell_hook_disabled=true + daemon disable. Binary opt-in kaldı (büyük İngilizce dosya). KRİTİK: hook temizlerken kullanıcının KENDİ hook'larını (KAPI/session-save/rm-guard) koru — sadece 'lean-ctx' içerenleri sil. Yedek: settings.json.bak-leanctx-20260727. Ders: token-tasarrufu aracı çalışmayı ENGELLERSE tasarruf negatiftir; ayrıca pkill -f "lean-ctx serve" kendi shell'ini öldürür → [l]ean bracket kullan (#18).

---
*Kaynak: lean-ctx v6 native-deny + Türkçe çökme 2026-07-27 → settings.json + .claude.json + CLAUDE.md + config.toml*
