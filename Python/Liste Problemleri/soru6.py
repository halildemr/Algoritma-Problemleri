#=============================================================================
# Bir listede ki elemanlarin kac tanesinin [1,5] araliginda oldugunu
# tespit eden algoritmayi fonksiyon seklinde kodlayiniz.
# [1,-12,1,-7,-27,25,42,51,53,3]
#=============================================================================
# Bu fonksiyona aktarılan listenin her zaman sayılardan oluştuğu varsayılmıştır.
# Aksi halde fonksiyon 12. ya da 16. satırda hata verecektir. 
#=============================================================================

def araliktaOlanlar( liste ):
    
    uzunluk = len( liste )
    sayac = 0
    
    for i in range(0,uzunluk):
        if liste[i] >= 1 and liste[i] <= 5 :
            sayac = sayac + 1
            
    return sayac
