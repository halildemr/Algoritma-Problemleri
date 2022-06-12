#=============================================================================
# Bir listedeki en buyuk ve en kucuk sayilarin farkini bulan
# algoritmayı kodlayiniz.
# [ 1,2,3,-1 ] 
# [1,2,3,0,0,11,25,-5,-3,21]
# [1,2,3,0,0,11,[1,2,True],25,-5,-3,21]

# HATA DURUMLARI:
    # Boş liste
    # Listenin tuple, str, list veri tiplerini içermesi
    # Fonksiyona int, float, bool veri tiplerinin aktarılması
#=============================================================================
# Bu algoritma en büyük ve en küçük sayıları indexleri kullanarak tespit eder
#=============================================================================

def fark( liste ):
    
    if type( liste ) == list:
        
        es = len( liste )
        
        if es != 0:
            
            enbuyuk = 0
            enkucuk = 0
            
            for i in range(1,es):
                if type(liste[i]) == int or type(liste[i]) == float:
                    if liste[i] < liste[enkucuk]:
                        enkucuk = i
                    if liste[i] > liste[enbuyuk]:
                        enbuyuk = i
                        
            return liste[enbuyuk] - liste[enkucuk]
        else:
            print('Liste boş')
        
    else:
        print('Veri tipi hatası')
