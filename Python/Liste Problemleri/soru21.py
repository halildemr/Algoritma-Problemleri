#=============================================================================
# Bir listenin elemanlarının benzersiz olup olmadığını tespit
# eden algoritmayı fonksiyon şeklinde kodlayınız.
# [1,2,3,4,5,6,7,8,9]
# [1,2,3,1,4,5,6,7,8,9]
# [1,2,3,7,4,5,6,7,8,9]
# Algoritma mantığı:
# ilk elemanı seç ve sağdaki elemanlarla sorgula
#=============================================================================


def elemanlarBenzersizmi( liste ):
    es = len( liste )
    
    for i in range(0,es-1):
        secilenEleman = liste[i]
        for j in range(i+1,es):
            sagdakieleman = liste[j]
            if secilenEleman == sagdakieleman:
                return False
            
    return True
