#=============================================================================
# Girilecek iki listenin eşit olup olmadığını kontrol eden
# algoritmayı kodlayınız
#
# Örnek:
# A = [9,8,7,6,5,4]
# B = [9,8,7,6,5,0] 
# Varsayım: 
#           Listenin elemanları sıralıdır.
# Koşullar:
#           İki listenin eleman sayısı eşit olmalı.
#           A = B olabilmesi her i için A(i) = B(i) olmalısıdır.
#=============================================================================
# Fonksiyona aktarılan değerlerlerden en az biri list değilse 21. ya da 22.
# satırlar için hata alınır. Bu nedenle fonksiyona aktarılan verilerin
# tip kontolü yapılmalıdır. Size bırakıyorum :)
#=============================================================================

def listelerEsitmi( liste1, liste2 ):
    
    es1 = len( liste1 )
    es2 = len( liste2 )
    
    if es1 == es2:
        for i in range(0,es1):
            if liste1[i] != liste2[i]:
                return False
        return True
        
    else:
        return False
