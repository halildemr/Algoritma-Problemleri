#=============================================================================
# Bir listede ki negatif elemanlarin toplamini bulan algoritmayi fonksiyon 
# seklinde kodlayınız.
#=============================================================================
# Birinci probleme özellik eklendi.
# Bu algoritma:
# Liste içindeki listelerin sahip olduğu negatif elemanları mevcut toplama
# ekler.
#=============================================================================

def  negatiflerinToplamiV1_2( liste ):
    
    if type( liste ) == list:
        
        es = len( liste )
        toplam = 0
        
        for i in range(0,es):
            
            if type(liste[i]) == list:
                toplam = toplam + negatiflerinToplamiV1_1( liste[i] )
                
            if ( type(liste[i]) == int or type(liste[i]) == float ) and liste[i] < 0:
                toplam = toplam + liste[i]
                
        return toplam
        
    else:
        print('Veri tipi hatası.')
    
    
def negatiflerinToplamiV1_1( L ):
    
    es = len( L )
    toplam = 0
    
    for i in range(0,es):
        if type(L[i]) == int or type(L[i]) == float:
            if L[i] < 0:
                toplam = toplam + L[i]
                
    return toplam
