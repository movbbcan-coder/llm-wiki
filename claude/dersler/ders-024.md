---
ureten: hafiza-yayinla
tip: ders
no: 24
etiketler: [ders, rulebook]
---

# Ders 24 — nginx'te tanımsız `server_name` (örn. ceo.movbbcan.com) 443'e gelince **default

nginx'te tanımsız `server_name` (örn. ceo.movbbcan.com) 443'e gelince **default server**'a düşer = alfabetik ilk enabled site. SNI testini `curl --resolve ad:443:127.0.0.1` ile yap (`-H Host:` SNI göndermez, yanıltır). Çözüm: her subdomain için ayrı server bloğu + self-signed cert (Cloudflare Full)

---
*Kaynak: CEO bot Panel'i dual_research dashboard açıyordu 2026-06-17 → /etc/nginx/sites-available/ceo-hub*
