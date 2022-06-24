#=============================================================================
# Bir listenin ilk iki elemanı belliyken 100 elemanlı olacak şekilde 
# güncellemeniz istenmektedir. Listenin ilk iki elemanı 10 ve 11 dir.
# Sonraki her eleman kendisinden önce gelen iki elemanın toplamıdır.
# Buna göre 100 elemanlı bir listeyi oluşturunuz.
# [10,11,21,32,53,85 ... ]
#=============================================================================


def listegenislet():
    
    liste = [ 10,11 ]
    
    x = 1
    while x <= 998:
        toplam = liste[x-1] + liste[x]
        liste.append( toplam )
        x = x + 1
        
    return liste
