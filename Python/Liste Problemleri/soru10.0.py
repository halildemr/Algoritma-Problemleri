#=============================================================================
# Bir x sayisini bir listenin elemanlariyla karsılastirip x'den kucuk olan liste
# elemanlarinin index numarasini konsola basan algoritmayi fonksiyon seklinde
# kodlayiniz.
# GİRDİ:   [125, 92, -5, 81, 21, 17, 32, 4, 0] , 20
# ÇIKTI:   [2,5,7,8] --> 20 den küçük olan sayıların indexleri
#=============================================================================
# Bu fonksiyona her zaman sayılardan oluşan bir listenin aktarılacağı 
# varsayılmıştır. Aksi halde 14. veya 17. satırda hata verecektir. 
#=============================================================================

def kucuklerinindexi( liste, x ):
    
    elemansayisi = len( liste )
    
    for i in range(0,elemansayisi):
        if liste[i] < x :
            print(i)
            
kucuklerinindexi( [125, 92, -5, 81, 21, 17, 32, 4, 0] , 20 )
