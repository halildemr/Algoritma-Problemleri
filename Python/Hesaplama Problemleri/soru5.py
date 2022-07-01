#================================================================
# Fonksiyona girilecek kenar sayısına göre düzgün
# dörtgenin, üçgenin ya da beşgenin alanını hesaplayan
# algoritmayı kodlayınız.
#================================================================


def kenaragorealan( kenar ):
    
    if kenar == 4:
        kenar1 = float( input('1. kenar uzunlugu...:'))
        kenar2 = float( input('2. kenar uzunlugu...:'))

        if kenar1 > 0 and kenar2 > 0:
            alan = kenar1 * kenar2
            print(alan)
        else:
            print('Negatif sayı girdiniz.')
        
        
    elif kenar == 3:
        taban    = float( input('Taban uzunlugu...:'))
        dikkenar = float( input('Dik kenar uzunlugu....:'))
        
        if taban > 0 and dikkenar > 0:
            alan = taban * dikkenar / 2
            print(alan)
        else:
            print('Negatif sayı girdiniz.')
        
        
    elif kenar == 5:
        besgeninkenari = float( input('Düzgün beşgenin bir kenarının uzunlugu...:'))
        dikkenar       = float( input('Dik kenar uzunlugu....:'))
        
        if besgeninkenari >0 and dikkenar > 0:
            alan = 5 * dikkenar * besgeninkenari / 2
            print(alan)
        else:
            print('Negatif sayı girdiniz.')

    else:
        print('Geçerli kenar bilgisini girmediniz.')
        
        
        
        
        
