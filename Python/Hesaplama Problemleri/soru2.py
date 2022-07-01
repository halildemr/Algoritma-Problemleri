#================================================================
# Çarpma işlemini toplama yoluyla hesaplayan algoritmayı
# kodlayınız.
#================================================================

def carp( x,y ):
    
    toplam = 0
    
    if x == 0 or y == 0 :
        print('Sonuc: 0')
        return
    
    if x < 0 and y < 0 :
        for i in range(0,-x):
            toplam = toplam + y
        print('Sonuc...:',-toplam)
        
    elif x > 0 and y > 0:
        for i in range(0,x):
            toplam = toplam + y
        print('Sonuc...:',toplam)
        
    elif x < 0 and y > 0:
        for i in range(0,-x):
            toplam = toplam + y
        print('Sonuc...:',-toplam)
        
    elif x > 0 and y < 0 :
        for i in range(0,x):
            toplam = toplam + y
        print('Sonuc....:',toplam)
