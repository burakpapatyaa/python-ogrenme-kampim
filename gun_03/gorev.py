# GÖREV
# 4. Kavrama scansu / Mini Görev
# Bir siber güvenlik senaryosu düşün. Aşağıdaki sözlük yapısında, port numaraları anahtar, servis isimleri ise değerdir:

# network_scan = {80: "HTTP", 443: "HTTPS", 22: "SSH"}

# Sana verilen görev:

# Bu sözlüğe 21: "FTP" bilgisini ekle.

# 80 portunun ismini "Apache HTTP" olarak güncelle.

# Kullanıcıdan bir port numarası girmesini iste ve eğer o port sözlükte varsa servis ismini yazdır, yoksa "Port bulunamadı" mesajı ver (çökme yaşanmasın).

import time
network_scan = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH"
}
time.sleep(0.5)
print("Program başlatılıyor...")
time.sleep(0.2)

print(f"Sözlük: {network_scan}")
time.sleep(1)

print("Sözlüğe veri ekleniyor...")
network_scan[21]= "FTP"
time.sleep(0.5)

print(network_scan)
time.sleep(0.5)

print("Veri güncelleme yapılıyor...")
time.sleep(0.5)
network_scan[80]= "Apache HTTP"
print(f"Güncel sözlük: {network_scan}")
time.sleep(0.5)

port_number = int(input("Bir port numarası girin: "))
print("Sorgulama yapılıyor...")
time.sleep(1)

if port_number in network_scan:
    print(f"Servis var: {network_scan[port_number]}")
else:
    print("Port bulunamadı!")