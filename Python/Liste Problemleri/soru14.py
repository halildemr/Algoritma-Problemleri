#=============================================================================
# Bir sayi listesinin her elemanini 5'e bolup kalanlariyla
# mevcut listeyi guncelleyen algoritmayı kodlayiniz.
#=============================================================================
# Fonksiyona her zaman sayılardan oluşan bir listenin verileceği
# varsayılmıştır. 
#=============================================================================

liste1 = [0,5,10,15,20,25,30,35,40,45,50,55,60]
liste2 = [1,6,11,16,21,26,31,36,41,46,51,56,61]
liste3 = [8,9,45,12,36,98,451,57,125,1,697,157831]

def guncelle( liste ):
    
    es = len( liste )
    index = 0
    while index <= es - 1:
        kalan = liste[index] % 5 
        liste[index] = kalan
        index = index + 1
        
    return liste
