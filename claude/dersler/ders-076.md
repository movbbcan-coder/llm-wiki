---
ureten: hafiza-yayinla
tip: ders
no: 76
etiketler: [ders, rulebook]
---

# Ders 76 — Bir aracın çıkış kodu "0" demesi işini yaptığı anlamına gelmez — ürettiği ÇIKTININ tazeliğini ölç.

**Bir aracın çıkış kodu "0" demesi işini yaptığı anlamına gelmez — ürettiği ÇIKTININ tazeliğini ölç.** `uiautomator dump` animasyonlu ekranda "could not get idle state" ile başarısız olur ama **RC=0** döner; döküm dosyası yazılmaz. Eski kod dosyayı silmeden `cat` ettiği için telefondaki **3 gün önceki** XML "şu anki ekran" diye sunuluyordu: `tel ui` üç gündür sessizce bayat ekran okuyordu ve kimse fark etmemişti (ekran görüntüsü ayrı yoldan geldiği için çelişki görünmüyordu). Yakalanma biçimi öğretici: çıktıya TAZE bir ikinci kaynak (`dumpsys topResumedActivity`) eklenince çelişki anında ortaya çıktı (liste denk diyor, ekran Termux diyor). **Kural: dış araçtan gelen dosyayı okumadan önce SİL; sonuç boşsa bayat veriyi SUNMA, arızayı söyle. Bir olguyu iki bağımsız kaynaktan okumak (liste + activity adı) en ucuz bayatlık dedektörüdür** (#34/#35 ailesi: denetleyemediğin hâl ayrı bir bulgudur).

---
*Kaynak: ccoto FAZ 0 telefon ajan döngüsü 2026-08-12 → tel_uzak.sh oku() + test_tel_uzak.sh (bayat kapısı)*
