#=============================================================================
# Bir listede kac tane sayinin oldugunu tespit eden algoritmayi fonksiyon
# seklinde kodlayiniz.
# [1,'A',1,'B','C',0,1,0,1.535,0.1524]
#=============================================================================

def kacsayivar( liste ):
    
    es = len( liste )
    sayac = 0
    
    for i in range(0,es):
        if type(liste[i]) == int or type(liste[i]) == float:
            sayac = sayac + 1
            
    return sayac 
