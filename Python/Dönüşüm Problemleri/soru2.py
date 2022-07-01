#=================================================================
# Bir tam sayıyı basamak değerlerinin toplamı şeklinde görüntüleyen 
# algoritmayı kodlayınız.
#
# Girdi -->  2250
# Çıktı -->  2000 + 200 + 50 + 0
#
# Algoritma işleyişi:
# 2250 = 2*10^3 + 2*10^2 + 5*10^1 + 0*10^0
# 2250 = 2*1000 + 2*100  + 5*10   + 0*1
#=================================================================

        
def matematik( sayi ):
    
    stringsayi = str( sayi )
    basamaksayisi = len( stringsayi )
    basamakdegeri = 10**( basamaksayisi - 1 )
    basamakListesi = []
        
    
    for i in range(0,basamaksayisi):
        basamak = int( stringsayi[i] ) * basamakdegeri
        basamakListesi.append( basamak )
        basamakListesi.append( '+' )
        basamakdegeri = basamakdegeri // 10
        
    print( basamakListesi )
    
    sonuc = ''
    es = len( basamakListesi )
    for j in range(0,es-1):
        sonuc = sonuc + str( basamakListesi[j] )
        
    print(sayi, '=',sonuc)
