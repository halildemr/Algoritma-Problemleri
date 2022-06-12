#=============================================================================
# Bir listedeki en buyuk ve en kucuk sayilarin farkini bulan
# algoritmayı kodlayiniz.
# [ 1,2,3,-1 ] 
# [1,2,3,0,0,11,25,-5,-3,21]
# [1,2,3,0,0,11,[1,2,True],'istanbul',25,-5,-3,21]
# [1,1,1,1,1,1]

# HATA DURUMLARI:
    # Boş liste
    # Listenin tuple, str, list veri tiplerini içermesi
    # Fonksiyona int, float, bool veri tiplerinin aktarılması
#=============================================================================
# Soru2.0 ın hataları giderilmiştir
#=============================================================================

def fark( liste ):
    
    if type( liste ) == list:
        
        es = len( liste )
        
        if es != 0:
            
            enbuyuk = liste[0]
            enkucuk = liste[0]
            for i in range(1,es):
                if type(liste[i]) == int or type(liste[i]) == float:
                    if liste[i] < enkucuk:
                        enkucuk = liste[i]
                    if liste[i] > enbuyuk:
                        enbuyuk = liste[i]
                    
            return enbuyuk - enkucuk
        else:
            print("Liste boş")
    else:
        print('Veri tipi hatası')
