# GÖREV
# daily_logs adında şu elemanları sırasıyla içeren bir liste oluştur:
# "LOGIN_SUCCESS", "FAILED_LOGIN", "DATA_REQUEST", "FAILED_LOGIN", "LOGOUT", "FAILED_LOGIN", "LOGIN_SUCCESS"

# suspicious_activities adında boş bir liste tanımla.

# daily_logs listesi üzerinde bir for döngüsü ile gezin. Eğer okunan log "FAILED_LOGIN" ise, bu kaydı suspicious_activities listesine append ile ekle.

# Döngü tamamlandığında, tespit edilen şüpheli işlem sayısını bir değişkene ata 
# (İpucu: Listenin eleman sayısını bulmak için len(suspicious_activities) fonksiyonunu kullanabilirsin).

# Son olarak bir while döngüsü kur. Şüpheli işlem sayısı 0'dan büyük olduğu sürece çalışsın. Ekrana "Şüpheli işlem inceleniyor... 
# Kalan analiz: [sayı]" yazdır ve her iterasyonda sayacı 1 azaltarak sonsuz döngüyü engelle.
import time
daily_logs = [
    "LOGIN_SUCCESS", "FAILED_LOGIN", "DATA_REQUEST", "FAILED_LOGIN", "LOGOUT", "FAILED_LOGIN", "LOGIN_SUCCESS"]
suspicious_activities = []

for log in daily_logs:
    if log == "FAILED_LOGIN":
        suspicious_activities.append(log)
        
print(suspicious_activities)
s_a_number = len(suspicious_activities)

while s_a_number > 0:
    time.sleep(0.5)
    print(f"Şüpheli işlem inceleniyor... Kalan analiz:  {s_a_number}")
    s_a_number-=1
