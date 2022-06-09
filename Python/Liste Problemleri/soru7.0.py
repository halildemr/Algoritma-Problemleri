#=============================================================================
# Öyle bir fonksiyon yazınız ki, x sayisindan buyuk olan liste elemanlarini 
# liste olarak versin
# [1,-12,1,-7,-27,25,42,51,53,3] x = 7
# [25,42,51,53]
#=============================================================================

def buyuklerinListesi( liste , x ):
    
    uzunluk = len( liste )
    yeniListe = []
    
    for i in range(uzunluk-1,-1,-1):
        if liste[i] > x:
            yeniListe.append( liste[i] )
            
    return yeniListe
