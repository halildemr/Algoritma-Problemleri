#================================================================
# Belirli bir sayıyı tespit etmeye çalışan sayı tahmin oyununu
# kodlayınız.
#================================================================

def sayitahminet():
    
    sayi = 19
    print('Tahminde bulunurken -1 girişi yaparak oyundan çıkabilirsiniz.')
    
    tahmin = int( input('Tahmininiz....: '))
    
    while True:
        
        if tahmin == sayi:
            print('Sayıyı buldunuz. Tebrikler')
            return
        elif tahmin == -1:
            print('Çıkış başarılı.')
            return
        else:
            tahmin = int( input('Tahmininiz....: '))
            
