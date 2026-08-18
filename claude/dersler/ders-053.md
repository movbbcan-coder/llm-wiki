---
ureten: hafiza-yayinla
tip: ders
no: 53
etiketler: [ders, rulebook]
---

# Ders 53 — Bir düzeltmeden sonra arıza SÜRÜYORSA, kaldırdığın şey suçlu DEĞİLDİ — geri al, yoksa çalışan özelliği bedavaya kaybedersin.

**Bir düzeltmeden sonra arıza SÜRÜYORSA, kaldırdığın şey suçlu DEĞİLDİ — geri al, yoksa çalışan özelliği bedavaya kaybedersin.** Termux çağrı sisteminde ekran donuyordu; şüpheli `tmux switch-client` (izin isteyen tmux oturumunu ekrana getiren satır) kaldırıldı — AMA sonraki testte donma AYNEN sürdü. Gerçek suçlu MacroDroid'in "Uygulama Başlat" bayraklarıydı ("Yeniyi zorla" + "Son uygulamalardan çıkar" işaretli → Termux'un çalışan mosh/tmux görevi yerine yeni instance zorlanıyor, uygulama açılıyor ama girdi odağı alamıyor). Bayraklar kaldırılınca donma bitti. Ben o arada rulebook'a "hook terminale dokunmasın" diye YANLIŞ ders yazmıştım — kaldırma ile düzelme arasında test yoktu, korelasyon uydurdum. **Kural: bir şeyi kaldırdıktan sonra arızanın gittiğini ÖLÇMEDEN ders yazma; arıza sürüyorsa kaldırdığını geri koy** (#35/#41 ailesi: ölçülmemiş öncül). switch-client geri eklendi, tedbir olarak ayrı süreçte + 2sn gecikmeli. YAN DERS: ntfy bildirim→MacroDroid "Bildirim Alındı" zinciri S24 Ultra'da (izinler açık) hiç tetiklenmedi; MacroDroid'i uzaktan tetiklemenin sağlam yolu **Webhook (URL)** tetikleyicisi — bildirim okuma/metin filtresi zincirini komple atlar (tanımlayıcıda boşluk/özel karakter kullanma).

---
*Kaynak: Termux çağrı sistemi 2026-07-29 → termux_push.sh + TERMUX_CAGRI.md*
