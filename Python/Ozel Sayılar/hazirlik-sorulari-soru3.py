#==================================================================
# Pozitif bir sayının pozitif tam bölenlerinin sayısını tespit
# edecek algoritmayı kodlayınız.
# ÖRNEK:
# YÖNTEM: 8 sayısı için { 1,2,3,4,5,6,7,8 }
# 8 sayısının pozitif tam bölenleri ---> 1,2,4,8 ---> 4 p.t.b
# 12 sayısının pozitif tam bölenleri --> 1,2,3,4,6,12 ---> 6 p.t.b
#==================================================================


def pozitifTamBolenSayisi( p ):
    
    adet = 0
    for i in range(1,p+1):
        if p % i == 0:
            adet = adet + 1
            
    return adet
