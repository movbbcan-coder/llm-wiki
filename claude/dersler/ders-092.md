---
ureten: hafiza-yayinla
tip: ders
no: 92
etiketler: [ders, rulebook]
---

# Ders 92 — Zaman aşımıyla kesilen SFTP aktarımı, boyutu DOĞRU ama içi delikli bir dosya bırakır — ve `adb install` ona "Success" der.

**Zaman aşımıyla kesilen SFTP aktarımı, boyutu DOĞRU ama içi delikli bir dosya bırakır — ve `adb install` ona "Success" der.** ccoto APK'sını telefona kuran araçta `timeout 120 scp` sabiti vardı; 24 MB'lık APK tünel üzerinden 120 saniyede bitmeyince timeout scp'yi ortada kesti. Modern `scp` SFTP konuşur ve rastgele erişimle yazdığı için hedef dosyanın **boyutu birebir doğru** göründü (24580711 = 24580711) — kısmi dosyanın küçük kalacağı sezgisi burada YANLIŞ. Sonra `adb install -r` bozuk APK'yı kabul edip **"Success"** yazdı; kurulum "başarılı" sanıldı, oysa cihazda çalışmayan bir sürüm vardı. Yakalayan tek şey md5 karşılaştırması oldu (kurulu paketin özeti ≠ gönderilen dosyanın özeti). **Kural: dosya aktarımını "boyut tuttu" ile doğrulama — ÖZET (md5/sha) karşılaştır; ve doğrulamayı KURULUMDAN ÖNCE yap, yoksa bozuk paket cihaza yazılmış olur.** İkinci kural: bir aktarımın zaman aşımı SABİT olamaz, dosya boyutuyla ölçeklenir (burada 60 sn taban + ~300 KB/s). Üçüncü: uzun süren bir kurulum betiğini kısa timeout'lu bir kabuk çağrısıyla başlatma — betiğin kendi kapıları (md5 kontrolü) çalışmadan süreç ölür ve geriye "exit 0" ile yarım iş kalır (#89 ailesi: RC=0 ≠ iş yapıldı).

---
*Kaynak: ccoto baloncuk APK kurulumu 2026-08-28 → tel_ortak.tel_scp_ver boyut-oranlı timeout + kur_ve_dogrula.sh gönderim-öncesi bütünlük kapısı*
