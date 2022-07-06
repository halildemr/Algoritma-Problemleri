#================================================================
# Pozitif bir aralıktaki sayılardan kaç tanesinin 9 rakamını 
# içerdiğini tespit eden algoritmayı kodlayınız.
#================================================================

def rakamsorgula( sayi1,sayi2 ):
    
    sayici = 0
    
    for i in range(sayi1,sayi2+1):
        
        stringsayi = str( i )
        basamaksayisi = len( stringsayi )
        
        for j in range(0,basamaksayisi):
            rakam = int( stringsayi[j] )
            
            if rakam == 9:
                sayici = sayici + 1
                break
    print(sayici)
