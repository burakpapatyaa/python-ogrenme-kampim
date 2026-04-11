# 11 Nisan 2026 - Çalışma Özeti

## İşlenen Konular
* Python Sözlük (Dictionary) Veri Yapısı ve Hash Table Çalışma Mantığı.
* Sözlüklerde CRUD (Ekleme, Okuma, Güncelleme, Silme) İşlemleri.
* Üyelik Testi (`in` operatörü) ile Hata Yönetimi.
* **Nested Structures:** Liste içindeki sözlük elemanlarına `liste[indeks]['anahtar']` mantığıyla erişim.
* Sözlük Metotları: `.items()`, `.keys()`, `.values()` ve Tuple Unpacking.
* Güvenli Veri Erişimi: `.get()` Metodu ve Overwriting (Üzerine Yazma) Kuralları.

## Kritik Noktalar
* **Erişim Verimliliği:** Sözlüklerin $O(1)$ erişim hızı ile listelerden farkı ve büyük verilerdeki (API/Log) önemi kavrandı.
* **Sayaç (Frequency Count) Mantığı:** Bir sözlükte anahtarın varlığını kontrol ederek değer artırma algoritması uygulandı.
* **Hiyerarşik Veri Analizi:** Firewall logları örneğinde, karmaşık (iç içe) veri yapılarından spesifik verilerin çekilmesi pratiği yapıldı.
* **Hata Toleransı (Fault Tolerance):** Olmayan bir anahtara erişirken programın çökmesini engellemek için `.get()` kullanımı ve varsayılan değer (fallback) atama mantığı pekiştirildi.
* **Anahtar Benzersizliği:** Sözlüklerde aynı anahtara yapılan atamaların eski veriyi güncellediği (Overwrite) siber güvenlik senaryosuyla deneyimlendi.

## Genel Değerlendirme
Öğrenci, gün boyunca sözlüklerin hem temel sözdizimini hem de ileri seviye kullanım senaryolarını başarıyla uyguladı. Özellikle siber güvenlik (IDS/Firewall/Log Analizi) odaklı problemlerde veriyi manipüle etme yeteneği oldukça güçlü. Yazım hatalarına (tuple yaratan gereksiz virgüller gibi) dikkat edildiği sürece kod kalitesi profesyonel standartlara yakındır.