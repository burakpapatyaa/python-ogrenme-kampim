# GÖREV

# incoming_traffic adında bir liste oluştur ve şu verileri gir:
# ["GÜVENLİ", "GÜVENLİ", "DDOS_ATTACK", "GÜVENLİ", "SQL_INJECTION", "XSS_PAYLOAD"]

# quarantine_zone adında boş bir liste tanımla.

# (Tespit Aşaması): incoming_traffic listesini bir for döngüsü ile dön. Eğer okunan veri "GÜVENLİ" değilse, bu veriyi doğrudan quarantine_zone listesine ekle (append).

# (İmha Aşaması): Karantina bölgesinde tehdit bulunduğu sürece çalışacak bir while döngüsü kur (İpucu: len(quarantine_zone) > 0 olduğu sürece).

# while döngüsünün içinde:

# Karantinadaki ilk elemanı (indeks 0) bir değişkene ata (current_threat = quarantine_zone[0]).

# Ekrana f"Tehdit imha ediliyor: {current_threat}" yazdır.

# İşlemi simüle etmek için time.sleep(1) kullan.

# O anki tehdidi quarantine_zone listesinden sil (remove).

# Karantina listesi tamamen boşalıp while döngüsü bittiğinde, ekrana "Tüm tehditler temizlendi. Sistem güvende." yazdır.

import time 
incoming_traffic = [
    "GÜVENLİ", "GÜVENLİ", "DDOS_ATTACK", "GÜVENLİ", "SQL_INJECTION", "XSS_PAYLOAD"
]

quarantine_zone = []

for i in incoming_traffic:
    if i!="GÜVENLİ":
        quarantine_zone.append(i)
traffic = len(quarantine_zone)



# while traffic > 0: #HATALI ve Riskli yaklaşım.
while len(quarantine_zone) > 0: 
    current_threat = quarantine_zone[0]
    print(f"Tehdit imha ediliyor: {current_threat}")
    quarantine_zone.remove(current_threat)
    time.sleep(1)

print("Tüm tehditler temizlendi. Sistem güvende.")