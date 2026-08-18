---
ureten: hafiza-yayinla
tip: ders
no: 70
etiketler: [ders, rulebook]
---

# Ders 70 — Cihaz otomasyonunda KULLANICI da bir değişkendir — "kendiliğinden oldu" demeden önce kullanıcıdan BAĞIMSIZ bir deney kur.

**Cihaz otomasyonunda KULLANICI da bir değişkendir — "kendiliğinden oldu" demeden önce kullanıcıdan BAĞIMSIZ bir deney kur.** Denk'in uygulama kilidi soğuk başlangıçta 1,5 sn içinde açılıyordu; `BASARILI tip=2` (device credential) logu üzerine "Samsung cihaz kilitsizken doğrulamayı atlıyor, CryptoObject'e geçmeliyiz" diye ciddi bir mimari değişikliğe gidilecekti. Kullanıcıya sorulunca gerçek çıktı: **telefon elindeydi, her seferinde parmak izi veriyordu.** Beş ölçüm de bu yüzden kirliydi. Kesin cevabı tek turda veren şey kullanıcıdan bağımsız deneydi: istemi `input keyevent 4` ile İPTAL et → `HATA kod=10` → kilit açılmadı → koruma kanıtlandı. **Kural: bir öznenin (kullanıcı, ağ, zamanlayıcı) müdahale edebildiği ölçümde önce müdahaleyi dışla ya da öncülü SOR; "dokunma" demek ölçüm garantisi değildir.** İkinci ders: teşhis için geçici `Log.i` eklemek (derle-kur-ölç, 1 dk) tahmin yürütmekten ucuzdur — üç turluk tahmin yerine tek satır iz kök nedeni verdi (#35/#53/#56 ailesi).

---
*Kaynak: Denk uygulama kilidi doğrulaması 2026-08-09 → DEVAM.md KARAR FAZ 0 tablosu*
