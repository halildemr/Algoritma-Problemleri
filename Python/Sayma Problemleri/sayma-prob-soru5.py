#================================================================
# İkilik tabanda girilecek bir sayıda kaç tane 1 olduğunu sayan
# algoritmayı kodlayınız.
#================================================================

def birlerisay( ikilik ):
    
    uzunluk = len( ikilik )
    sayici = 0
    
    for i in range(0,uzunluk):
        if ikilik[i] in ['1','0']:
            if ikilik[i] == '1':
                sayici = sayici + 1
        else:
            print('Girdiğiniz ifade ikilik tabanda değil.')
            return 
        
    return sayici
