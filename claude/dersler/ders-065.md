---
ureten: hafiza-yayinla
tip: ders
no: 65
etiketler: [ders, rulebook]
---

# Ders 65 — "Bu metin konuyla ilgili değil" ile "konuyla ilgili AMA OLMADI" ayrı sınıflardır; ikisini aynı listeye koyarsan biri ötekini yer.

**"Bu metin konuyla ilgili değil" ile "konuyla ilgili AMA OLMADI" ayrı sınıflardır; ikisini aynı listeye koyarsan biri ötekini yer.** İki yönlü hata aynı gün çıktı. (a) Gürültü listesi kalıplardan ÖNCE çalışıyordu ve içinde `"giriş yapıldı"` vardı — bankacılıkta "giriş" hem OTURUM AÇMA hem PARA GİRİŞİ demek; tutarı ve bakiyesi düzgün okunan gerçek bir para bildirimi hiç denenmeden çöpe gidiyordu. Gürültü SON ÇARE yapıldı: tutarı kesin okunan kalıp kazanır. (b) Ters yönde, *"878.75 TL … ödemeniz gerçekleşmedi"* bildirimi tutarı ve hesabı olan gerçek bir para metnidir ama işlem OLMAMIŞTIR — bugün hiçbir kalıba uymadığı için güvendeyiz, fatura kalıbı eklendiği gün hayalet gider yazacaktı. Ayrı bir **olumsuzluk kapısı** eklendi (kalıp uysa bile kaydetme). Kelimeler uydurulmadı, canlı 78 bildirimle sınandı (1 eşleşme, o da tam bu vaka) ve eski/yeni motor karşılaştırıldı: **0 kayıt farkı**. İNCELİK: yalın "iptal" bilerek listeye alınmadı — *"iptal edilen işleminiz için X TL iade edilmiştir"* gerçek bir para GİRİŞİDİR. Aynı JSON'u iki dil okuyorsa (Kotlin+Python) kapı İKİSİNE de eklenmeli, yoksa sessizce ayrışırlar.

---
*Kaynak: Denk kalıp motoru 2026-08-09 → bank_patterns.olumsuzluk + KalipMotoru + motor.py + OlumsuzlukTest*
