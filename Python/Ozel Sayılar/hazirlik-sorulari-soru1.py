#=================================================================
# Bir tam sayının rakamlarının birbirinden farklı olup olmadığını
# tespit eden algoritmayı kodlayınız.
# 12343
# 1==2 1==3 1==4 1==3
# 2==3 2==4 2==3
# 3==4 3==3
# 4==3
#=================================================================

def rakamlarFarklimi( x ):
    
    stringsayi = str( x )
    
    for i in range(0,len(stringsayi)):
        
        for j in range(i+1,len(stringsayi)):
            
            if stringsayi[i] == stringsayi[j]:
                return 0
            
    return 1
