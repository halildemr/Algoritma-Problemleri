#================================================================
# Bir tam sayının son basamağını kontrol ederek 2'ye veya 5'e 
# tam bölünebildiğini ya da bölünemediğini söyleyen algoritmayı
# kodlayınız.
#================================================================


def bolunurmu( sayi ):
    
    stringsayi = str( sayi )
    sonbasamak = int( stringsayi[ len(stringsayi)-1 ])
    
    if sonbasamak == 0:
        print('Girilen sayı 2 ye ve 5 e tam bölünür')
    elif sonbasamak in [2,4,6,8]:
        print('Girilen sayı 2 ye tam bölünür.')
    elif sonbasamak == 5:
        print('Girilen sayı 5 e tam bölünür.')
    else:
        print('Girilen sayı 2 ye veya 5 e tam bölünmez.')
        
