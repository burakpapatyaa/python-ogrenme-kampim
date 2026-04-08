# GÖREV
# Bir ağ trafiği izleme simülasyonu yazmanı istiyorum:

# incoming_ips adında, içinde en az 6 farklı IP adresi (string) bulunan bir liste oluştur. 
# İçlerinden bir tanesi bilinen zararlı IP olan "192.168.1.99" olsun.

# blocked_ips adında boş bir liste oluştur.

# incoming_ips listesini for ile dön.

# Eğer dönülen IP adresi "192.168.1.99" ise bunu doğrudan blocked_ips listesine append ile ekle ve ekrana "DİKKAT: Zararlı IP engellendi!" yazdır. 
# (Diğer IP'ler için sadece "IP temiz: [IP Adresi]" yazdır).

# Bu işlem bittikten sonra, bir while döngüsü kullanarak sistemin güvenlik duvarını yeniden başlatma simülasyonu yap. 
# Ekrana 3 defa (sayaç ile) "Güvenlik Duvarı Yeniden Başlatılıyor..." yazdır.

import time

incoming_ips = ["192.168.1.96", 
                "192.168.1.97", 
                "192.168.1.98", 
                "192.168.1.99", 
                "192.168.1.100", 
                "192.168.1.101"
                ]
blocked_ips = []

#sayac=3 #Hatalı değil ama değiştirilmeli
# PEP-8 ve Clean Code standartları gereği bir projede dil bütünlüğü korunmalıdır (Örn: restart_counter)
restart_counter = 3

for ip in incoming_ips:
    # print(f"Taranıyor:  {ip}")
    time.sleep(0.5)
    print("-" * 30)
    if ip == "192.168.1.99":

        # Altta ki kod hatalıdır, çünkü o satırda veri elle girilmiş, döngüde ki referans kullanılmalı
        # blocked_ips.append("192.168.1.99") #--HATALI
        blocked_ips.append(ip)

        print("-" * 30)

        # Altta ki kod Liste tek elemanlıyken çalışır ancak listeye 50 tane zararlı IP eklendiğinde, her yeni engellemede geçmişteki 49 IP'yi de ekrana basar,
        # bu yüzden o an ki işlemi loglamak için -f string ile ip değişkeni kullanılmalıdır.
        # print("DİKKAT: Zararlı IP engellendi! IP Adresi: ", *blocked_ips) #RİSKLİ
        print(f"DİKKAT: Zararlı IP engellendi! IP Adresi: {ip}")

        time.sleep(1)
        print("-" * 30)
        print("-" * 30)
    else:
        print(f"IP temiz: {ip}")
        print("-" * 30)

while restart_counter > 0:
    time.sleep(1)
    print("Güvenlik Duvarı Yeniden Başlatılıyor...")
    restart_counter-=1