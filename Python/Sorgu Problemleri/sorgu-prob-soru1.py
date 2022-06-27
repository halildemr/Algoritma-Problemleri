#================================================================
# Girilen 3 farklı sayıdan ortancayı tespit eden algoritmayı
# kodlayınız.
#================================================================

def ortanca( x , y , z ):
    
    sonuc = farkliMi( [x,y,z] )
    
    if sonuc == True:
        if ( y <= x and x <= z) or ( z <= x and x <= y):
            print('Ortanca....:', x)
            
        elif (x <= y and y <= z) or ( z <= y and y <= x):
            print('Ortanca....:', y)
            
        elif ( x <= z and z <= y) or ( y <= z and z <= x):
            print('Ortanca....:', z)
    else:
        print('Sayılar farklı değil.')


def farkliMi( L ):
    
    for i in range(0,2):
        
        for j in range(i+1,3):
            if L[i] == L[j]:
                return False
    return True
