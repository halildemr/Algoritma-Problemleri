#=================================================================
# Pozitif bir sayının rakamlarının toplamını bulan 
# algoritmayı kodlayınız.
#=================================================================

def basamaklarinToplami( x ):
    
    if x > 0:
        stringsayi = str( x )
        
        toplam = 0
        for i in range(0,len(stringsayi)):
            rakam = int( stringsayi[i] )
            toplam = toplam + rakam
            
        return toplam
    else:
        print('Girilen sayı negatif')
        return -1 
