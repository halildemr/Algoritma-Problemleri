#================================================================
# Üs alma işlemini çarpma yoluyla gerçekleştiren algoritmayı
# kodlayınız.
# Varsayım: üs >= 1
#
# Girdi -->  taban, us
# Çıktı -->  x reel sayısı
#================================================================


def usal( taban, us ):
    
    if us >= 1:
        carpim = 1
        for i in range(0,us):
            carpim = carpim * taban
        print('Sonuc....:',carpim)
        
    else:
        print('İşlem başarısız.')
