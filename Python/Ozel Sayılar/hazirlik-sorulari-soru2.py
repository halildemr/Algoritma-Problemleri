#=================================================================
# Bir sayının basamaklarında ki rakamlarından çift olanların 
# sayısını verecek algoritmayı kodlayınız.
#=================================================================


def ciftSayiAdedi( y ):
    
    stringsayi = str( y )
    uzunluk = len( stringsayi )
    sayac = 0
    
    for i in range(0,uzunluk):
        basamak = int( stringsayi[i] )
        if basamak % 2 == 0:
            sayac = sayac + 1
            
    return sayac
