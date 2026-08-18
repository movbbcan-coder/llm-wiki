---
ureten: hafiza-yayinla
tip: ders
no: 75
etiketler: [ders, rulebook]
---

# Ders 75 — Devir notu KONUŞMAYI değil ÜRÜNÜ taşımalı — ve "yayınlandı mı?" sorusunu yeni hesap SORAMAZ.

**Devir notu KONUŞMAYI değil ÜRÜNÜ taşımalı — ve "yayınlandı mı?" sorusunu yeni hesap SORAMAZ.** claude2 %91'de claude1'e geçti; not son isteği + son yanıtı taşıdı ama oturumun ürettiği **artifact adreslerini taşımadı**. Yeni oturum `Artifact action:list` çağırdı ve öz-eleştiri artifact'ını GÖREMEDİ — çünkü **galeri hesaba bağlıdır**, claude2'de yayınlanan 4 artifact (`acd32838`, `056338f5`, `408622b6`, `bbf93344`) claude1'den ne listelenir ne güncellenir. Sonuç: "yayınlanamadan koptu" diye yanlış teşhis + aynı dosyanın **ikinci kopyası** yayınlandı (`6f790a13`). Gerçekte yayın 04:35'te tamamlanmıştı; kopan şey URL'i kullanıcıya söyleyen CÜMLEYDİ (transcript'te duruyordu, kullanıcı hiç görmedi). İkinci kayıp: **scratchpad oturuma özeldir**, yeni oturum boş dizinle başlar → üretilmiş dosyalar yolu yazılmazsa öksüz. Üçüncü ve en sinsisi: not YALNIZ geçiş anında yazılıyordu; **iki hesap da doluysa geçiş olmaz ve hiç not yazılmaz** (#32 ailesi: koruyucu tam ihtiyaç anında susar). Fix: tek yazıcı `/root/bin/devir-notu` (SSOT; prompt-auto-switch'teki KOPYA yazıcı silindi — #45), %80 bandından itibaren HER turda yazılır, içinde yayınlanan artifact URL'leri + teslim edilmemiş üretimler + sonucu dönmemiş çağrı + scratchpad yolu + kalıcı kopya var. Kural: bir devir mekanizması "ne konuştuk"u değil **"ne ürettim ve nerede duruyor"**u taşımalı; ve hesaba bağlı her kaynak (artifact galerisi, oturum dizini) geçişte GÖRÜNMEZ olur — adresi nota yaz.

---
*Kaynak: claude2→claude1 geçişinde artifact çift yayını 2026-08-10 → /root/bin/devir-notu + stop-auto-switch BAND_LO=80 + prompt-auto-switch kopya yazıcı kaldırıldı + claude-switch-prepare PREP_LO 85→80 + session-start bayat-not kapısı*
