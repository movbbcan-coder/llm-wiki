---
ureten: hafiza-yayinla
tip: ders
no: 61
etiketler: [ders, rulebook]
---

# Ders 61 — nginx'te regex `location` bloğu, önek bloğundan ÖNCE eşleşir — yönlendirmen sessizce es geçilir.

**nginx'te regex `location` bloğu, önek bloğundan ÖNCE eşleşir — yönlendirmen sessizce es geçilir.** Eski gizlilik adresini yeni alan adına 301'lemek için `location /denk/ { return 301 ...; }` yazdım; tetiklenmedi, 404 döndü. Sebep: aynı config'teki `location ~* \.html$` (cache başlığı için) regex olduğu için önce eşleşiyor ve isteği dosya sisteminden servis etmeye çalışıyor. Çözüm `location ^~ /denk/` — `^~` regex denemesini iptal eder (config'in kendi `/files/` bloğu da aynı sebeple öyle yazılmış, yani cevap zaten dosyanın içindeydi). Ayrıca: yeni subdomain'e KENDİ server bloğu + kendi self-signed cert'i şart (Cloudflare Full), yoksa 443 default server'a düşer (#24); SNI testi `curl --resolve ad:443:127.0.0.1` ile yapılır. **Kural: nginx'te bir location beklediğin gibi davranmıyorsa önce EŞLEŞME ÖNCELİĞİNE bak (exact `=` > `^~` > regex > önek), config'in kendi mevcut bloklarını örnek al.**

---
*Kaynak: Denk gizlilik politikası yayını 2026-07-30 → sites-available/denk + movbbcan `^~ /denk/`*
