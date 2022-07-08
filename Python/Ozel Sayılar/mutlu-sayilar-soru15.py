#========================================================================
# 2 - 100 arasındaki Mutlu sayıları tespit eden python kodlarını
# yazınız.
# [8, 64, 52, 29, 85, 89, 145, 42, 20, 4, 16, 37, 58, 89, 145, 42, 20, 4]
#========================================================================


def mutlusayilar():
    
    for i in range(2,101):
        
        kareListesi = [ i ]
        
        while True:
            
            soneleman = kareListesi[ len(kareListesi) - 1 ]
            toplam = karelerintoplami( soneleman )
            kareListesi.append( toplam )
            
            if kareListesi[ len(kareListesi) - 1 ] == 1:
                print('Mutlu sayÄ±...: ',i)
                break
            elif tekrarvarmi( kareListesi ) == 1:
                break
            
            
def tekrarvarmi( liste ):
    
    uzunluk = len( liste )
    soneleman = liste[ uzunluk - 1]
    for i in range(0,uzunluk - 1):
        if liste[i] == soneleman:
            return 1
    return 0



def karelerintoplami( sayi ):
    stringsayi = str( sayi )
    tplm = 0
    for i in range(0,len(stringsayi)):
        rakam = int( stringsayi[i] )
        tplm = tplm + rakam**2
    return tplm 
    
