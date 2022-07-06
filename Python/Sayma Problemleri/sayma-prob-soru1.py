#================================================================
# Bir karakter topluluğunda geçen x karakterinin sayısını verecek 
# algoritmayı kodlayınız.
#================================================================


cumle = """Bir karakter topluluğunda geçen x karakterinin sayısını verecek 
algoritmayı kodlayınız."""

def karaktersay( c,x=' '):
    
    karaktersayisi = len( c )
    sayici = 0
    
    for i in range(0,karaktersayisi):
        if c[i] == x:
            sayici = sayici + 1
            
    print('İlgili cümlede '+x+' karakteri '+str(sayici)+' kere geçmekte')

    
    
    
