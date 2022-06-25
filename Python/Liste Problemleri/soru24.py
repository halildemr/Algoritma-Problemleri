#=============================================================================
# Bir dizinin elemanlarına min - max normalizasyonunu uygulayan algoritmayi
# fonksiyon seklinde kodlayiniz.
# Formül:
#
#    L(i)   - min(V)
#   -----------------
#    max(V) - min(V)
#
# FORMÜLÜ İŞLEVSİZ KILAN LİSTELER: [] [1] [1,1] 
#=============================================================================

veri1 = [ 9856124,2165379,1241136,1245679,1034498,1033492,
        2356448,9523145,7784113,8523626,1245637,7411471 ]
veri2 = [25,30,23,32,27,29,40,42]


def minMaxNormalizasyon( V ):
    
    EBek = enbuyukEnkucuk( V )
    
    if EBek == 0:
        return 0
    else:
        minn = EBek[0]
        maxx = EBek[1]
        es = len( V )
        V1 = []
        for i in range(0,es):
            sonuc = ( V[i] - minn ) / ( maxx - minn )
            V1.append( sonuc )
        
        return V1

def enbuyukEnkucuk( L ):
    
    es = len( L )
    
    if es > 1:
        
        enbuyuk = L[0]
        enkucuk = L[0]
        
        for i in range(1,es):
            if L[i] < enkucuk:
                enkucuk = L[i]
            if L[i] > enbuyuk:
                enbuyuk = L[i]
        
        return [enkucuk, enbuyuk]
        
    else:
        return 0
