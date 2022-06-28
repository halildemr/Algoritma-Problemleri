#=================================================================
# Aşağıdaki şekil 6 satırdan oluşmaktadır. Fonksiyona verilecek y 
# sayısı için y satırdan oluşan görüntüyü elde edecek algoritmayı 
# kodlayınız.
#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********
# Bilgi: Bosluk sayısı....: (2*y)/2 - 1 = satirsayisi - 1
#=================================================================

# BİLGİLER:
# Her satırda yıldız karakteri artarken boşluk karakteri azalmaktadır.
# Yıldız karakterlerinin sağında ve solunda belli miktarda boşluk vardır.
# Yıldız karakterleri her satırda 2şer 2şer artmaktadır.
# Her satırın sağında ve solunda (satirsayisi - 1) / 2 kadar boşluk vardır.

def yildizlar( satirsayisi ):
    
    bosluksayisi = satirsayisi - 1
    yildizsayisi = 1
    
    for i in range(0,satirsayisi):
        
        yildiz = yildizsayisi * '*'
        satir = bosluksayisi * ' ' + yildiz + bosluksayisi * ' '
        print(satir)
        yildizsayisi = yildizsayisi + 2
        bosluksayisi = bosluksayisi - 1
