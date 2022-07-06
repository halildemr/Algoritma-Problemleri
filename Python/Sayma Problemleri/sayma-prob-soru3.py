#================================================================
# Bir listede ki negatif, pozitif ve sıfırları sayan ve bunların
# adetlerini ekranda görüntüleyen algoritmayı kodlayınız.
# [1,986,-12.5,3.14,-1,0,1,25,39,98,51,0,2,6,-5,6,-152]
#================================================================
liste = [1,986,-12.5,3.14,-1,0,1,25,39,98,51,0,2,6,-5,6,-152]
def spnsay(  l ):
    
    elemansayisi = len( l )
    saymaListesi = [0,0,0]
    
    for i in range(0,elemansayisi):
        
        if l[i] > 0 :
            saymaListesi[0] = saymaListesi[0] + 1
        elif l[i] < 0:
            saymaListesi[1] = saymaListesi[1] + 1
        elif l[i] == 0:
            saymaListesi[2] = saymaListesi[2] + 1
            
    print('Pozitiflerin sayısı....:',saymaListesi[0])
    print('Negatiflerin sayısı....:',saymaListesi[1])
    print('Sıfırların sayısı......:',saymaListesi[2])
    
    
    
    
