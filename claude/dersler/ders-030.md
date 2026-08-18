---
ureten: hafiza-yayinla
tip: ders
no: 30
etiketler: [ders, rulebook]
---

# Ders 30 — Yeni bir PARA dosyası eklersen conftest korumasına da ekle.

**Yeni bir PARA dosyası eklersen conftest korumasına da ekle.** banka_hareket.json eklendi ama tests/conftest.py'deki "canlı dosyaya yazma" kalkanına girmedi → test süiti CANLI deftere 22 sahte kayıt yazdı (havuz tesadüfen kurtuldu: o test kendi BB_DOSYA'sını temp'e çeviriyordu — koruma tesadüfe kalmıştı).

---
*Kaynak: test sızıntısı 2026-07-14 → tests/conftest.py*
