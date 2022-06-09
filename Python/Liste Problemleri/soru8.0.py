#=============================================================================
# Fonksiyona aktarilacak listede belirli bir eleman var mi sorusuna cevap 
# ureten algoritmayı kodlayiniz.
# [1,-12,1,-7,-27,25,42,51,53,3] , 'a'
# 'a' in [1,2,3,4,'a']
#=============================================================================


def elemanVarmi( A, y ):
    
    elemanSayisi = len( A )
    
    for i in range(0,elemanSayisi):
        if A[i] == y:
            return True
    return False


sonuc = elemanVarmi( [] , 'a' )
