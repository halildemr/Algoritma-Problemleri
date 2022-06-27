#================================================================
# Bir kişinin yaş bilgisine göre 
# çocuk - genç - orta yaşlı ve yaşlı sınıflamasını aşağıdaki
# durumlara göre kodlayınız.
# yaş: [0-12) çocuk
# yaş: [12-35) genç
# yaş: [35-55) orta yaşlı
# yaş: 55>= ise yaşlı
#================================================================

def siniflandirma( yas ):
    
    if yas >= 0 and yas < 12:
        print('Çocuk')
    elif yas >= 12 and yas < 35:
        print('Genç')
    elif yas >= 35 and yas < 55:
        print('Orta yaşlı')
    elif yas >= 55:
        print('Yaşlı')
