#================================================================
# Öğrencinin aldığı vize ve final notlarına göre dersten geçip 
# geçmediğini söyleyen algoritmayı kodlayınız.
# vize: %40 final: %60 geçme notu: 50 ve üzeri
#================================================================

def ders( vize, final ):
    
    if (vize >= 0 and vize <=100 ) and (final >= 0 and final <= 100):
    
        vize = vize*0.4
        final = final*0.6
        sonuc = vize + final
        if sonuc >= 50:
            print('Geçtiniz...:',sonuc)
        else:
            print('Kaldınız...:',sonuc)
        
    else:
        print('Vize ya da final notlarından en az biri yanlış girildi.')
        
        
