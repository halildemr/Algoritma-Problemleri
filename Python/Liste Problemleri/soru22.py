#=============================================================================
# Bir listenin tekrarlayan elemanlarını silerek elemanları 
# benzersiz bir dizi oluşturan algoritmayı kodlayınız.
# 
# [1,2,3,4,5,6,7,8,9]
# [1,1,2,3,4,5,6,7,8,9]
# [1,2,3,4,5,6,7,7,8,9]
#=============================================================================



def listeyiBenzersizYap( liste ):
    
    if elemanlarBenzersizmi(liste) == 1:
        return liste
    else:
        adres = 0
        while True:
            
            es = len( liste )
            indexListesi = []
            # Tekrarlayan elemanların indexlerinin tespiti
            for i in range(adres+1,es):
                if liste[adres] == liste[i]:
                    indexListesi.append(i)
            adres = adres + 1    
            
            uzunluk = len( indexListesi )
            
            if uzunluk > 0:
                # Tekrarlayan elemanların silinmesi
                sayi = 0
                while sayi <= uzunluk-1:
                    liste.pop(indexListesi[sayi] - sayi)
                    sayi = sayi + 1
     
            if elemanlarBenzersizmi(liste) == 1:
                return liste
                
                
        return liste
    
    

def elemanlarBenzersizmi( liste ):
    
    es = len( liste )
    
    for i in range(0,es-1):
        for j in range(i+1,es):
            if liste[i] == liste[j]:
                return 0
        
    return 1
