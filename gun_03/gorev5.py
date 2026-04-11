# GÖREV:
# Bir siber güvenlik API'sinden tehdit logları çekiyorsun ama paketlerin bazı kısımları eksik geliyor (bazılarında "risk_seviyesi" verisi var, bazılarında yok).

# Aşağıdaki kodu baz al:

# Python
# api_log = {"ip": "172.16.8.9", "tehdit_turu": "Malware"}
# Görev:

# Yukarıdaki sözlüğe "tehdit_turu" anahtarını kullanarak "Ransomware" değerini ata (Üzerine yazma kuralını tetikle).

# .get() metodunu kullanarak "risk_seviyesi" anahtarını çek. Sözlükte olmadığı için varsayılan olarak "Düşük" değerini getirmesini sağla.

# Bu işlemlerin ardından ekrana sadece şunu yazdır: 
# "IP: 172.16.8.9 - Risk: Düşük" (Buradaki IP ve Risk verisini dinamik olarak sözlükten / değişkenden çekmelisin).

api_log = {
    "ip": "172.16.8.9",
    "tehdit_turu": "Malware"
    }

api_log["tehdit_turu"] = "Ransomware"
risk = api_log.get("risk_seviyesi", "Düşük")
print(f"IP: {api_log['ip']} - Risk:  {risk}")