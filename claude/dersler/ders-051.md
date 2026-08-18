---
ureten: hafiza-yayinla
tip: ders
no: 51
etiketler: [ders, rulebook]
---

# Ders 51 — Güvenlik guard'ı saf-substring kullanırsa hem legit işi hem sadece-bahsi engeller — komut-pozisyonu + sınır farkındalığı şart.

**Güvenlik guard'ı saf-substring kullanırsa hem legit işi hem sadece-bahsi engeller — komut-pozisyonu + sınır farkındalığı şart.** pre-tool-use.sh `'rm -rf /root' in cmd` yapıyordu → `rm -rf /root/altdizin` (LEGIT, proje silerken quote'la aşmak zorunda kaldım) VE `grep "rm -rf /root"` (sadece METİN) engelleniyordu. Fix: danger_check.py — rm KOMUT-POZİSYONUNDA mı (`^`/`;`/`&&`/`|` sonrası) + yol ÜST-DÜZEY mi (alt-dizin serbest, lookahead sınır) regex; grep/echo bahsi ile gerçek komut ayrışır. 23-vaka birim test (danger_check_test.py). Ders: bir guard "yanlış-pozitif" ürettikçe kullanıcı onu baypas etmeyi öğrenir (quote hilesi) = guard aşınır; guard'ı komut yapısına duyarlı yaz, metne değil.

---
*Kaynak: rm-guard substring friction 2026-07-27 → danger_check.py + pre-tool-use.sh + test*
