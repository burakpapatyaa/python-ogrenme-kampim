# Gün 1: Python Temelleri ve Mimari Mantık (Değişkenler, Karar Yapıları, Truthiness)

**Tarih:** 7 Nisan 2026, Salı

## İşlenen Konuların Özeti
Bugün, programlamanın temel yapı taşları olan değişkenler, veri tipleri ve kontrol akışlarını (if/elif/else) sadece sözdizimi (syntax) olarak değil, siber güvenlik ve yazılım mimarisi perspektifinden ele aldık. Bellek yönetimi mantığı, Python'ın "Truthiness" (doğruluk/yanlışlık) felsefesi, mantıksal operatörler (`and`, `or`, `not`) ve yetkilendirme mekanizmalarının (WAF, RBAC) arka planında yatan çalışma prensipleri üzerine pratik senaryolarla (giriş simülasyonu, güvenlik duvarı, rol bazlı erişim) kod geliştirdik.

## Öğrenilen Kritik Noktalar
* **Tip Dönüşümleri (Type Casting):** `input()` fonksiyonu varsayılan olarak her zaman `String` (metin) döndürür. Matematiksel işlemler için veriyi `int()` veya `float()` ile dönüştürmek şarttır. `input()` zaten string döndürdüğü için onu tekrar `str()` içine almak gereksiz bir işlemdir (Redundancy).

* **Atama vs Karşılaştırma:** `=` operatörü bellekteki değişkene değer atar, `==` operatörü ise iki değerin eşitliğini sorgular ve geriye boolean (True/False) döner.

* **Truthiness (Doğruluk Mantığı):** Python'da `0`, boşluk (`""`) ve `None` (hiçlik) arka planda `False` kabul edilir; dolu olan her şey `True`'dur. Sıfırın bir matematiksel değer, None'ın ise verisizlik olduğunu unutmamak gerekir.

* **Pythonic Kontroller:** Profesyonel kodlamada `if degisken == True:` veya `== False:` yazılmaz. Sadece `if degisken:` veya `if not degisken:` şeklinde, değişkenin doğrudan kendi durumu sorgulanır. Performans ve okunabilirlik için elzemdir.

* **Default Deny Prensibi:** Güvenlik mimarilerinde sadece beklenen ve izin verilen kesin durumlar (`if`/`elif`) kodlanmalı, geri kalan tüm belirsiz, eksik ve geçersiz durumlar `else` bloğunda reddedilmelidir.

* **İşlem Önceliği:** `and` ve `or` operatörleri aynı şartta (satırda) kullanılacaksa, güvenlik zafiyetlerini ve mantık hatalarını önlemek için mutlaka parantez `()` ile gruplandırma yapılmalıdır.

## Performans Değerlendirmesi ve Tavsiyeler
**Genel Performans:** Mükemmel. İş kurallarını (Business Logic) koda dökme konusunda çok başarılısın. Özellikle hata yaptığında veya bir mantığı yanlış anladığında, o hatanın arka planını sorgulaman ve detaya inmek istemen gerçek bir "Yazılım Mimarı" refleksi. Kodlarına eklediğin yorum satırlarının *ne* yaptığını değil, *neden* yaptığını açıklaması sektördeki kıdemli (Senior) geliştiricilerin yaklaşımıdır; bu vizyonu korumalısın. Analitik zekan ve kendi kodunu refactor etme (iyileştirme) hızın çok yüksek.

**Gelecekte Dikkat Etmen Gerekenler:**
* **Logic Bug (Mantık Hataları):** Sözdizimini (syntax) hatasız yazsan da, özellikle `not` operatörüyle çalışırken şartların kablolarını ters bağlamamaya dikkat etmelisin. Şartları yazdıktan sonra mutlaka "Şu an içeri banlı olanı mı alıyorum, yoksa temiz olanı mı?" diye kodunu zihninde Türkçe bir cümle gibi sesli okuyarak test et.
* **Sadelik (Zen of Python):** Gereksiz veri tipi dönüşümleri veya `else` ile bitirilebilecek bir durumu tekrar `elif` ile uzatmak gibi durumlardan kaçınarak kodunu olabildiğince minimalist tutmaya odaklan.