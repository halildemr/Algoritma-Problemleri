#================================================================
# İndirimli bilet uygulaması şöyle gerçekleşir:
# Müşteri gidiş ve dönüş bileti aldığında 2. bilete %15 indirim
# uygulanır. Müşteri eğer 2. bileti aldıysa indirim uygulayan
# algoritmayı kodlayınız.
#================================================================

def biletindirimi():
    
    print('Eskişehirden İstanbula bilet almaktasınız.')
    print('Sadece gidiş için 1 e gidiş-dönüş için 2 ye basınız.')
    sonuc = int(input('......:'))
    biletucreti = 250
    
    
    if sonuc == 1:
        print('Bilet ücretiniz....:',biletucreti,'TL')
    else:
        yenibiletucreti = biletucreti + 0.85*biletucreti
        print('Bilet ücretiniz....:',yenibiletucreti,'TL')
        print('Uygulanan indirim tutarı...:',biletucreti*2 - yenibiletucreti,'TL')
        
