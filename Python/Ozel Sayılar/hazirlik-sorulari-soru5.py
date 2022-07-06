#=================================================================
# Bir sayının basamak sayısının tek ya da çift olma durumana göre
# ilgili sayıyı iki parçaya ayıran algoritmayı kodlayınız.
# Sayı çift basamaklı ise ---> 1234 ---> 12-34
# Sayı tek basamaklı ise  ---> 12345 --> 123-45
#=================================================================


def parcayaAyir( y ):
    
    stringsayi = str( y )
    uzunluk = len( stringsayi )
    
    p1 = ''
    p2 = ''
    
    if uzunluk == 1:
        return y
    elif uzunluk % 2 == 0:
        for i in range(0,int(uzunluk/2)):
            p1 = p1 + stringsayi[i]
            
        for j in range(int(uzunluk/2),uzunluk):
            p2 = p2 + stringsayi[j]
            
        return p1,p2
    else:
        for i in range(0,int(uzunluk/2)+1):
            p1 = p1 + stringsayi[i]
            
        for j in range(int(uzunluk/2)+1,uzunluk):
            p2 = p2 + stringsayi[j]
            
        return p1,p2
