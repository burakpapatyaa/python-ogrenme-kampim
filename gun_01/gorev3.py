# GÖREV
# Şu iki değişkeni başlangıç olarak tanımla:
# user_role = "editor"  (Test ederken bunu "admin", "mod" veya "guest" yaparak dene)
# is_banned = False     (Bunu da True yaparak güvenlik duvarını test et)

# Şartlarımız:

# (Önce Güvenlik): Eğer kullanıcı banlıysa (is_banned True ise), 
# rolü ne olursa olsun "Sistemden uzaklaştırıldınız!" yazdır.

# (Yetki Kontrolü): Kullanıcı banlı DEĞİLSE ve rolü "admin" VEYA "mod" ise
# "Yönetim Paneline Hoş Geldiniz" yazdır. (Yukarıda verdiğim parantez ipucunu unutma!)

# (Default Deny / Standart Akış): Eğer banlı değilse ama yetkisi de "admin" veya "mod" değilse 
# (yani sadece "editor" veya "user" ise), "Standart Sayfa Yükleniyor..." yazdır.

user_role = "editor"
is_banned = False



# Altta ki ilk kod hatalıdır, çünkü bu şart eğer "kullanıcı banlı değilse" demektir, bu durumda masum kullanıcılar içeri alınmaz :)
# if not is_banned: 
if is_banned:
    print("Sistemden uzaklaştırıldınız!")

# Altta ki ilk kod hatalıdır çünkü bu şart eğer "kullanıcı banlı ise ..." diye ilerler, bizim başlangıçta ki değişken değeri ile işimizi yok, sadece o an ki kontrolü yapmalıyız.
# elif is_banned and (user_role=="admin" or user_role=="mod"):
elif not is_banned and (user_role=="admin" or user_role=="mod"):
    print("Yönetim Paneline Hoş Geldiniz")

else:
    print("Standart Sayfa Yükleniyor...")