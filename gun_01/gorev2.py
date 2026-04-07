# GÖREV
# İki adet manuel değişken oluştur: is_ip_blacklisted ve has_valid_token. 
# Bunlara başlangıçta True veya False değerlerini ver (kodunu test ederken bu değerleri değiştirip denersin).

# Şartlarımız şunlar:

# Eğer gelen IP kara listedeyse (is_ip_blacklisted True ise), 
# kullanıcının token'ı (jetonu) geçerli olsa bile hiçbir şeye bakmadan ekrana "Bağlantı koparıldı: IP kara listede!" yazdır.
#  (İpucu: Bu en kritik ve öncelikli güvenlik kontrolüdür, ilk sırada olmalı).

# Eğer IP kara listede DEĞİLSE ve has_valid_token True ise "Sunucuya erişim sağlandı." yazdır.

# Eğer IP kara listede DEĞİLSE ama has_valid_token False ise "Kimlik doğrulama hatası!" yazdır.

# Kural: Bu görevde == True veya == False kullanmak yasak. 
# Sadece değişkenlerin kendi doğruluğunu (truthiness) ve gerekirse not operatörünü kullanacaksın.




is_ip_blacklisted = True
has_valid_token = False


# Eğer IP karalistedeyse ne olursa olsun engelle!
if is_ip_blacklisted:
    print("Bağlantı koparıldı: IP kara listede!")

# Eğer IP karalistede değilse ve token doğruysa içeri al.


# Altta ki ilk kod hatalıdır çünkü if her zaman True kontrolü yapar, bu koda göre parolayı doğru giren kullanıcılar 
# sistemden geçemezken yanlış girenler geçecektir, o yüzden aşağıda ki gibi olmalı, 
# eğer parola True ise girebilir, False ise giremez, parola değişkeninin içinde ne yazdığ bizi ilgilendirmez, 
# biz o an ki durumu inceleriz.


# elif not is_ip_blacklisted and not has_valid_token:
elif not is_ip_blacklisted and has_valid_token:
    print("Sunucuya erişim sağlandı.")




# YÖNTEM 1
# Eğer IP karalistede değilse ama token hatalıysa doğrulama hatası ver.
# elif not is_ip_blacklisted and has_valid_token:
#     print("Kimlik doğrulama hatası!")

# # Eğer bunlardan hiçbiri değilse başak bir hata vardur, ekrana Hata! yaz.
# else:
#     print("Hata!")


# YÖNTEM 2

else:
    print("Kimlik doğrulama hatası!")

# Yöntem olarak ikinciyi seçtim çünkü zaten yazılan diğer şartlar tamamlanmazsa geriye bir ihtimal kalıyor, o da else olur, 
# gereksiz yere kodu uzatmak sadece işlem kalabalığı olur.