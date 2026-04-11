# GÖREV
# Bir "Saldırı Tespit Sistemi" (IDS) simülasyonu yapalım:

# blocked_ips adında bir sözlük oluştur. İçine "192.168.1.1": "Brute Force" ve "10.0.0.5": "SQL Injection" kayıtlarını at.

# Sisteme yeni bir tehdit algılandığını varsay: "172.16.0.100" IP adresini "DDoS" açıklamasıyla sözlüğe ekle.

# Kullanıcıdan bir IP adresi al.

# Eğer bu IP sözlükte varsa, saldırı tipini ekrana yazdır ve "Erişim Engellendi" de.

# Eğer yoksa, bu IP'yi "Güvenli" açıklamasıyla sözlüğe ekle ve "Erişim İzin Verildi" yazdır.


import time
blocked_ips = {
    "192.168.1.1": "Brute Force",
    "10.0.0.5": "SQL Injection"
}
time.sleep(0.5)
print(f"Mevcut durum: Engellenen IP Adresleri---->  {blocked_ips}")

time.sleep(1)

print("Sistem taraması yapılıyor...")
time.sleep(1.5)
print("Yeni tehdit bulundu!")

blocked_ips["172.16.0.100"] = "DDoS"
time.sleep(1)
print(f"Tehdit engellendi!")
time.sleep(0.5)

ip = input("Bir IP adresi giriniz: ")

if ip in blocked_ips:
    print(f"{blocked_ips[ip]} Erişim Engellendi!")
else:
    blocked_ips[ip] = "Güvenli"
    print("Erişim İzni Verildi!")
time.sleep(1)
print(f"Mevcut liste: {blocked_ips}")

