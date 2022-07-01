#=================================================================
# Basamak sayısı 8 i geçen her tam sayıyı bilimsel formatta 
# görüntüleyen algoritmayı kodlayınız.
#
# Girdi -->  15.000.000.000
# Çıktı -->  1.5e+10
#=================================================================

def bilimselgoruntule( sayi ):
    
    stringsayi = str( sayi )
    basamaksayisi = len( stringsayi )
    
    if basamaksayisi > 8:
        
        soldanilkbasamak = stringsayi[0]
        soldanikincibasmak = stringsayi[1]
        kalanbasamaksayisi = basamaksayisi - 1
        print(soldanilkbasamak + '.' + soldanikincibasmak + 'e+' + str(kalanbasamaksayisi))   
        
    else:
        print( sayi )
        
