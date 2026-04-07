# Görev: Basit bir yetkilendirme sistemi yaz.

# Sistemde geçerli ve sabit bir şifre belirle (örneğin: "AI_Cyber2026").
# Kullanıcıdan input() ile sırasıyla doğum yılını ve şifresini iste.
# Kullanıcının yaşını, mevcut yıldan doğum yılını çıkararak dinamik olarak hesapla.

# Şartlar:

# Eğer şifre doğruysa VE hesaplanan yaş 18'e eşit veya büyükse ekrana "Tam Erişim" yazdır.
# Eğer şifre doğruysa VE yaş 18'den küçükse "Sınırlı Erişim" yazdır.
# Eğer şifre yanlışsa (yaşa bakmaksızın) "Erişim Engellendi" yazdır.




# Öncelikle parolayı tanımlıyoruz
sifre = "Deneme_123"

# Kullanıcıdan aldığımız doğum yılı ile matematiksel işlem yapılacak, o yüzden int alıyoruz.
dogum_yili = int(input("Doğum yılınız giriniz: "))


# parola = str(input("Parolanızı giriniz: "))   
parola = input("Parolanızı giriniz: ")
# input() zaten default olarak string veri alır, tekrar str yazarak vakit kaybetmeye gerek yoktur.




yas = 2026 - dogum_yili


# Python da if/elif için paranteze gerek yoktur, şartları direk yazabilirsin.
# if (yas>=18 and parola==sifre):
if yas >= 18 and parola == sifre:
    print("Tam Erişim")

# elif(yas < 18 and parola == sifre):
elif yas < 18 and parola == sifre:
    print("Sınırlı Erişim")

else:
    print("Erişim Engellendi")