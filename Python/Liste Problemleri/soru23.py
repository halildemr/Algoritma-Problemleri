#=============================================================================
# Bir listeyi tersine ceviren algoritmayı kodlayiniz.
# [ 1,2,3,4,5,6,7,8,9 ] ---> [ 9,8,7,6,5,4,3,2,1 ] 4 işlem
# [ 1,2,3,4,5,6,7,8 ]   ---> [ 8,7,6,5,4,3,2,1 ]   4 işlem
#=============================================================================

def terscevir( liste ):
    
    es = len( liste )
    
    solindex = 0
    sagindex = es - 1
    
    x = 1
    while x <= int( es/2 ):
        
        gecici            = liste[ solindex ]
        liste[ solindex ] = liste[ sagindex ]
        liste[ sagindex ] = gecici
        
        solindex = solindex + 1 
        sagindex = sagindex - 1
        
        x = x + 1
        
    print( liste )
    
