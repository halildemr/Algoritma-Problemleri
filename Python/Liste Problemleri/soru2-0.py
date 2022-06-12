#=============================================================================
# Bir listede ki en buyuk ve en kucuk sayilarin farkini bulan algoritmayı 
# fonksiyon seklinde kodlayiniz.

# [1,2,3,0,0,11,25,-5,-3,21]    
# GİRDİ: liste
# ÇIKTI: eb - ek = x

# HATA DURUMLARI:
    # Boş liste
    # Listenin tuple, str, list veri tiplerini içermesi
    # Fonksiyona int, float, bool veri tiplerinin aktarılması
#=============================================================================
# soru2.1'e giderek hataların çözümüne ulaşabilirsiniz.

def fark( liste ):
    
    es = len( liste )
    
    enbuyuk = liste[0]
    enkucuk = liste[0]
    
    for i in range(1,es):
        if liste[i] < enkucuk:
            enkucuk = liste[i]
        if liste[i] > enbuyuk:
            enbuyuk = liste[i]
            
    return enbuyuk - enkucuk
