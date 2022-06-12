#=============================================================================
# Bir listede ki negatif elemanları pozitife ceviren algoritmayı
# kodlayınız.
# [1,-12,1,-7,-27,25,42,51,53,3]
#=============================================================================
# Bu fonksiyona aktarılan listenin her zaman sayılardan oluştuğu varsayılmıştır.
# Aksi halde fonksiyon 12. ya da 16. satırlarda hata verecektir. 
#=============================================================================

def pozitifeCevir( liste ):
    
    uzunluk = len( liste )
    print( liste )
    
    for i in range(0,uzunluk):
        if liste[i] < 0:
            liste[i] = -liste[i]
    
    print(liste)
