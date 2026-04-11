# GÖREV:


# Bilinen zararlı IP'ler ve tehdit türleri
threat_intel = {
    "192.168.1.50": "Ransomware",
    "10.0.0.99": "DDoS Botnet",
    "203.0.113.5": "APT Group"
}

# İzin verilen güvenli portlar
allowed_ports = [80, 443, 22]

# Sunucuya gelen anlık bağlantı istekleri (Ağ trafiği logları)
# Bu veri yapısı, içinde sözlükler barındıran bir listedir (List of Dictionaries)
incoming_requests = [
    {"ip": "192.168.1.10", "port": 80},
    {"ip": "10.0.0.99", "port": 443},
    {"ip": "192.168.1.50", "port": 22},
    {"ip": "172.16.0.5", "port": 3389},
    {"ip": "192.168.1.10", "port": 443},
    {"ip": "10.0.0.99", "port": 80},
    {"ip": "203.0.113.5", "port": 21},
    {"ip": "10.0.0.99", "port": 22}
]

# Görev Adımları:
# Sistemde engellenen saldırgan IP'lerin kaç kez engellendiğini tutmak için attack_counts adında boş bir sözlük oluştur.

# incoming_requests listesi üzerinde bir döngü başlat ve her bir isteği (dictionary) incele.

# Filtre 1 (Tehdit İstihbaratı): İstek yapan "ip", threat_intel sözlüğünde varsa:

# Ekrana tehdit tipini ve IP'yi yazdır (Örn: "DDoS Botnet engellendi: 10.0.0.99").

# Bu IP'yi attack_counts sözlüğüne ekle. Zaten varsa sayısını 1 artır, yoksa 1 olarak başlat.

# Filtre 2 (Port Kontrolü): Eğer IP temizse (tehdit sözlüğünde yoksa), "port" numarasının allowed_ports listesinde olup olmadığını kontrol et.

# İzin verilmeyen bir portsa ekrana yazdır (Örn: "Yetkisiz port denemesi engellendi. IP: 172.16.0.5, Port: 3389").

# Geçiş İzni: IP temizse VE port izin verilenler listesindeyse bağlantıya izin ver. (Örn: "Bağlantı başarılı: 192.168.1.10:80")

# Raporlama: Döngü bittiğinde, attack_counts sözlüğünü kullanarak ekrana "Gün Sonu Saldırı Raporu"nu yazdır (Hangi IP kaç kez engellenmiş).

# İpucu: attack_counts sözlüğünde sayacı artırırken, anahtarın önceden var olup olmadığını in operatörü ile kontrol etmen gerekecek.


import time 

attack_counts = {}

ip = 'ip' #Hatalı değil ama değiştirilmeli
port = 'port' #Hatalı değil ama değiştirilmeli
# bunlar yerine yerine doğrudan i['ip'] ve i['port'] kullanmak PEP-8 standartlarına daha uygundur ve okunabilirliği artırır.
ip_adress= []

for i in incoming_requests:

    if i[ip] in threat_intel:
        time.sleep(1)
        print(f"{threat_intel[i[ip]]} engellendi: {i[ip]}")
        if i[ip] in attack_counts:
            attack_counts[i[ip]] += 1
        else:
            attack_counts[i[ip]] = 1

    elif not i[port] in allowed_ports:
        time.sleep(1)
        print(f"Yetkisiz port denemesi engellendi. IP: {i[ip]}, Port: {i[port]}")
        if i[ip] in attack_counts:
            attack_counts[i[ip]] += 1
        else:
            attack_counts[i[ip]] = 1

    else:
        time.sleep(1)
        print(f"Bağlantı başarılı: {i[ip]}")

time.sleep(1)
print("\nGÜN RAPORU: ")
time.sleep(1)
print("YÜKLENİYOR...")
time.sleep(2)
for c in attack_counts:
    print(f"Bu IP: {c} toplam da {attack_counts[c]} kez engellendi!")
    time.sleep(0.1)


