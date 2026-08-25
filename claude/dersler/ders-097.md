---
ureten: hafiza-yayinla
tip: ders
no: 97
etiketler: [ders, rulebook]
---

# Ders 97 — Tek bir denetimsiz süreç, tüm VPS'i devirebilir — ve devrilme "her şey çöktü" diye görünür.

**Tek bir denetimsiz süreç, tüm VPS'i devirebilir — ve devrilme "her şey çöktü" diye görünür.** Kullanıcı sabah "her şey çöktü" dedi; ölçüm: 31 servisin hepsi 2 dakikalık, 10'u kapalı, yük ortalaması 34.98. Zincir: **04:18:35 OOM-killer** (`dmesg -T | grep oom-kill`) → öldürdüğü süreç Bybit lamba **Chrome**'u → PM2 daemon da gitti → systemd 04:24'te `pm2 resurrect` çalıştırdı → bellek hâlâ dipteyken 10 servis ayağa kalkamadı. Yani kök neden "sunucu çöktü" değil, **tek bir tarayıcının sınırsız büyümesiydi**: ölçümde 12 süreç · cgroup'a göre 712 MB (ps'in RSS toplamı 3,6 GB gösteriyordu — paylaşımlı belleği çift sayar, **cgroup `MemoryCurrent` gerçek olandır**). Chrome bayrakları YETMEZ: `--js-flags=--max-old-space-size` yalnız V8 heap'ini, `--renderer-process-limit` bu sürümde hiçbir şeyi sınırlamadı. Tek gerçek tavan cgroup: `systemd-run --scope -p MemoryHigh=700M -p MemoryMax=900M -p MemorySwapMax=0` → aşarsa YALNIZ o süreç ölür, sistem ayakta kalır. Kural: **7/24 çalışan yardımcı bir süreç (tarayıcı, headless render, scraper) mutlaka cgroup tavanı altında koşmalı**; "şu an az yiyor" ölçümü yeterli değildir, tavanı olmayan süreç er ya da geç komşularını öldürür. TEŞHİS SIRASI (bu vakada işe yarayan): `pm2 list` (hepsi aynı yaşta mı? → toplu restart) → `uptime` (yük) → `dmesg -T | grep -i oom` (kim öldürdü) → `systemctl status pm2-root` (daemon ne zaman kalktı) → `ps --sort=-rss` (kim şişirdi). YAN DERS (kendi hatam): "dump'ta kapalı kaydedilmişti" diye rapor ettim, sonra `dump.pm2`'yi açıp baktım — **status alanı hiç yok**, çıkarım uydurmaydı; dosyayı okumadan yapı hakkında hüküm kurmuşum (#83 ailesi: iddiayı ölçmeden yazma). Düzeltildi. İKİNCİ YAN DERS: makinede 16 Claude süreci vardı, üçü 296-532 SAATTİR açık (~540 MB atıl) — uzun ömürlü ajan oturumları sessiz bellek borcudur, periyodik olarak yaşlarına bakılmalı.

---
*Kaynak: VPS OOM çöküşü 2026-08-25 → bybit_lamba/basla.sh cgroup tavanı + pm2 dump yedeği/save*
