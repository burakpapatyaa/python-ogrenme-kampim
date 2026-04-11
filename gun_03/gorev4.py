# GÖREV:
# Aşağıdaki sözlükte bir web sunucusuna gelen hata kodları ve sayıları tutuluyor:
# error_logs = {"404": 15, "500": 2, "403": 8}

# Görev: .items() metodunu kullanarak bu sözlük üzerinde bir döngü kur ve eğer hata sayısı 5'ten büyükse ekrana şunu yazdır:
# "KRİTİK HATA: [Hata Kodu] kodu [Hata Sayısı] kez alındı!"

error_logs = {"404": 15, "500": 2, "403": 8}

for error, count in error_logs.items():
    if count > 5:
        print(f"KRİTİK HATA: {error} kodu {count} kez alındı!")


# !!!NOT!!!
# .keys(): Sadece anahtarları (IP'ler, Portlar, Hata Kodları) verir.

# .values(): Sadece değerleri (Saldırı sayıları, Durum açıklamaları) verir.

# .items(): İkisini birden bir çift (tuple) olarak verir. for k, v in dict.items() yazımı,
#  bu çifti anında iki ayrı değişkene parçalayarak (unpacking) işlem yapmanı sağlar.
#    Kodun hem daha hızlı çalışmasını hem de daha temiz görünmesini sağlar.