---
ureten: hafiza-yayinla
tip: ders
no: 78
etiketler: [ders, rulebook]
---

# Ders 78 — "Uygulama bozuk" sanılan davranış çoğu zaman terminal PROTOKOLÜDÜR — hangi ekran modunda olduğunu sor.

**"Uygulama bozuk" sanılan davranış çoğu zaman terminal PROTOKOLÜDÜR — hangi ekran modunda olduğunu sor.** Telefonda (Termux→mosh→tmux→Claude Code) parmakla kaydırma cc-* oturumlarında ekranı kaydırmıyor, **prompt geçmişini geri getiriyordu**; düz Termux kabuğunda ise sorunsuz çalışıyordu. Bu fark teşhisin kendisiydi: normal ekranda terminal kendi tamponunu kaydırır, **alternatif ekranda tampon yoktur → kaydırma OK TUŞUNA çevrilir** → TUI onu "geçmişte gezin" diye okur (ekranda `History 12/13` göründü). Yani ne Termux bozuktu ne tmux: `~/.tmux.conf`'ta `mouse on` zaten açıktı ve tmux'un fare bağlaması varsayılandı (`copy-mode -e`) — ok tuşunu tmux üretmiyordu. Uygulamayı değiştirmek (Termius/JuiceSSH) bu sınıfı ÇÖZMEZ. Çözüm uygulamanın kendi söylediğiydi: Claude Code ekranda *"Scroll wheel is sending arrow keys - use PgUp/PgDn to scroll"* yazıyordu — yani **cevap zaten ekrandaydı, üç tur boyunca okunmadı**. `~/.termux/termux.properties` → `extra-keys`'e PGUP/PGDN eklendi. Doğrulama sırası önemliydi: önce "PgUp gerçekten kaydırıyor mu?" boş bir pane'de ölçüldü (20 satır değişti), SONRA tuş eklendi — tersi olsaydı çalışmayan bir tuş eklenmiş olurdu. YAN DERSLER: (a) teşhis videosu 3,6 sn'lik mp4'tü; **GIF gönderilseydi tek kare gelirdi** (ölçüldü: GIF hem Read'de hem Gemini'de yalnız ilk kare, üstelik 5,3× büyük) — hareket gereken kanıtta mp4 ver, ben `fps=1 + tile` ile kontakt sayfası yapıp tek okumada görürüm (gizli veri Google'a gitmez); (b) `telmod`'u kapatınca çağrı hook'ları anında otomasyonu devirdi (#64 birebir tekrar) — cihaz sürerken AÇ, bitince KAPA; (c) `otodokun` canlı Claude TUI'sinde döküm alamayıp dokunmayı REDDETTİ (#76 kapısı doğru çalıştı) → **animasyonlu ekranda metinle dokunma çalışmaz, koordinat + ekran görüntüsü gerekir**.

---
*Kaynak: Termux scroll = ok tuşu 2026-08-12 → ~/.termux/termux.properties + ccoto FAZ 3 notu*
