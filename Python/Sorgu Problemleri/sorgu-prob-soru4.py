#================================================================
# [1,7] aralığında girilecek bir tam sayı için gün bilgisini
# geri döndüren algoritmayı kodlayınız.
#================================================================

def gunsoyle( n ):
    
    if n >= 1 and n <= 7:
        
        if n == 1:
            print('Pazartesi')
        elif n == 2:
            print('Salı')
        elif n == 3:
            print('Çarşamba')
        elif n == 4:
            print('Perşembe')
        elif n == 5:
            print('Cuma')
        elif n == 6:
            print('Cumartesi')
        elif n == 7:
            print('Pazar')
    else:
        print('1-7 aralığında bir sayı girmediniz.')
    
for i in range(1,8):
    gunsoyle( i )
