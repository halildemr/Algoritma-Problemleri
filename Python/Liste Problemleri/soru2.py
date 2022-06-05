#=============================================================================
# Bir listede ki negatif elemanlarin toplamini bulan algoritmayi fonksiyon 
# seklinde kodlayınız.
# [1,2,3,0,0,'Eskisehir','istanbul',[-1,-2,3],-5,-3,21]

# HATA DURUMLARI:
    # Listenin tuple, str, list veri tiplerini içermesi
    # Fonksiyona int, float, bool veri tiplerinin aktarılması
#=============================================================================
# Soru1 in hataları giderilmiştir.
#=============================================================================

def negatiflerinToplamiV1_1( liste ):
    
    if type( liste ) == list:
        
        es = len( liste )
        toplam = 0
        
        for i in range(0,es):
            if type(liste[i]) == float or type(liste[i]) == int:
                if liste[i] < 0:
                    toplam = toplam + liste[i]
                    
        return toplam
        
    else:
        print('Veri tipi hatası')
        
