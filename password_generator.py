import random

def main():
    karakterler_guclu = "abcdefghijklmnoprstuvyzqw0123456789ABCDEFGHIJKLMNOPRSTUVYZQW!@#$%^&*()?"
    karakterler_zayif = "abcdefghijklmnoprstuvyzqw0123456789"
    karakterler_listesig = list(karakterler_guclu)
    karakterler_listesiz = list(karakterler_zayif)
    sifre_sorgu = int(input("Güçlü bir şifre mi yoksa zayıf bir şifre mi istersiniz? Güçlü şifre için '1'e, zayıf şifre için '2'ye basın: "))

    if sifre_sorgu == 1:
        uzunluk = int(input("Şifre uzunluğunuz ne kadar olsun: "))
        secilenler = random.sample(karakterler_listesig,uzunluk)
        sifre = "".join(secilenler)
        print(f"Şifreniz: {str(sifre)}\n")
            
    elif sifre_sorgu == 2:
        uzunluk = int(input("Şifre uzunluğunuz ne kadar olsun: "))
        secilenler = random.sample(karakterler_listesiz,uzunluk)
        sifre = "".join(secilenler)
        print(f"Şifreniz: {str(sifre)}\n")

    else:
        print("Lütfen talimatlara uyarak doğru giriş yapınız!")
    
if __name__ == "__main__":
    main()