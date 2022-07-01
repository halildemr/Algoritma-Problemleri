#================================================================
# x. ayın y. günü yılın kaçıncı günüdür? İlgili algoritmayı 
# kodlayınız.
#   [31,29,31,30,31,30,31,31,30,31,30,31]
#================================================================



def gunsay( ay,gun ):
    
    aylarinGunsayilari = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    if ay >= 1 and ay <= 12:
        
        if gun <= aylarinGunsayilari[ay-1]:
            toplam = 0
            for i in range(0,ay-1):
                toplam = toplam + aylarinGunsayilari[i]
                
            sonuc = toplam + gun
            print('Yılın ',sonuc,'.günü')
        else:
            print('Gün bilgisi yanlış')
    else:
        print('Ay bilgisi yanlış')
