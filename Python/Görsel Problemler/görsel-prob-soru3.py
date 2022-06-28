#=================================================================
# [1,10] aralığında girilecek bir tam sayı için çarpım tablosu
# üreten algoritmayı kodlayınız.
# Kullanıcı 7 girdiyse 7'ler tablosu üretilecek
#=================================================================

def carpimtablosu( n ):
    
    if n >= 1 and n <= 10:
        for i in range(1,11):
            print(n,'x',i,'=',n*i)
