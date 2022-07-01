#================================================================
# x + 2y + 3z = 0 denklemini sağlayan değerleri [-25,25] 
# aralığındaki tam sayılar için tespit ediniz.
# Eşitliği sağlayan bütün değerlerin sayısını bulunuz.
#================================================================


def matematik():
    
    sayici = 0
    for x in range(-25,26):
        
        for y in range(-25,26):
            
            for z in range(-25,26):
                
                sonuc = x + 2*y + 3*z
                if sonuc == 0:
                    sayici = sayici + 1
                    print(x,y,z)
                    
    print('x+2y+3z = 0 eşitliğini sağlayan ',sayici,' x y z üçlüsü vardır')
    
