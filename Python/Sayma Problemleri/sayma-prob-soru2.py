#================================================================
# Bir karakter topluluğunda ki sesli harfleri sayan algoritmayı
# kodlayınız.
#================================================================

cumle = """Bir karakter topluluğunda ki sesli harfleri sayan algoritmayı
kodlayınız."""

def sesliHarfsay( c ):
    
    karaktersayisi = len( c )
    sayici = 0
    
    for i in range(0,karaktersayisi):
        if c[i] in ['a','e','ı','i','o','ö','u','ü']:
            sayici = sayici + 1
            
    return sayici

  
  
