#=================================================================
# Girilecek n m sayıları için n,m aralığında ki KIT sayıları
# tespit edecek python kodlarını yazınız. n,m pozitif tam sayı
#=================================================================


def kıtSayilar(n,m):
    
    for i in range(n,m+1):
        sonuc = pozitifToplamlar(i)
        
        if sonuc < i:
            print(i)
            
            
def pozitifToplamlar( x ):
    toplam = 0
    for i in range(1,x):
        if x % i == 0:
            toplam = toplam + i
    return toplam
