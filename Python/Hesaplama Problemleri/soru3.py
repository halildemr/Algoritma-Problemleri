#================================================================
# Kartezyen koordinat sisteminde bir noktanın orjine olan 
# uzaklığını hesaplayan algoritmayı kodlayınız.
#================================================================

def noktaninuzakligi( x=0, y=0 ):
    
    if x == 0 and y == 0:
        return 0
    else:
        uzaklik = (x**2 + y**2)**(1/2)
        return uzaklik
