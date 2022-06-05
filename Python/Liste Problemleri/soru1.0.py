#=============================================================================
# Bir listede ki negatif elemanlarin toplamini bulan algoritmayi fonksiyon 
# seklinde kodlayınız.

# [1,2,3,0,0,11,25,-5,-3,21] --> -8   
# GİRDİ: liste
# ÇIKTI: bir reel sayı

# HATA DURUMLARI:
    # Fonksiyona aktarılacak listenin tuple, str, list gibi veri tiplerini 
    # içermesi
        # ÖRNEK:
        # negatiflerinToplamiV1_0( [1,2,'a'] ) --> TypeError
    # Fonksiyona int, float, bool veri tiplerinin aktarılması
        # ÖRNEK:
        # negatiflerinToplamiV1_0( 987 ) --> TypeError
#=============================================================================
# Soru1.1'e giderek bu hataların çözümünü bulabilirsiniz. 


def negatiflerinToplamiV1_0( liste ):
    
    es = len( liste )
    toplam = 0
    
    for i in range(0,es):
        if liste[i] < 0:
            toplam = toplam + liste[i]
            
    return toplam
    
