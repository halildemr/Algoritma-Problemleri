#================================================================
# Girilecek bir sayının 3'e bölünüp bölünmediğini kontrol eden
# algoritmayı kodlayınız.
#================================================================


def uceBolunuyormu( sayi ):
    
    stringsayi = str( sayi )
    basamaksayisi = len( stringsayi )
    
    toplam = 0
    for i in range(0,basamaksayisi):
        toplam = toplam + stringsayi[i]
        
    if toplam % 3 == 0:
        return 1
    else:
        return 0
