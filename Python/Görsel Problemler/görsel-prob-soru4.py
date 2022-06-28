#=================================================================
# 3 sayısı için aşağıdaki şekilde görüntüleme elde edilmektedir.
# 0
# 01 
# 012
# 0123
# 012
# 01
# 0
# [0,9] aralığında ki bir sayı için benzer görüntüyü oluşturan 
# algoritmayı kodlayınız.
# toplam satır sayısını veren formül:  satirSayisi = y = 2*x + 1
# x fonksiyona girilen sayı
#=================================================================


def goruntu( sayi ):
    
    if sayi >= 0 and sayi <= 9:
        
        satirsayisi = 2*sayi + 1 ### toplam satır sayısı hesaplandı
        karaktersayisi = 1       ### oluşturulacak satırların karakter sayısını izler
        sınır = 0                ### satırda ki eleman sayısının ne zaman düşdüğünü izler
        
        for i in range(0,satirsayisi):
            satirstringi = ''
            for j in range(0,karaktersayisi):
                satirstringi = satirstringi + str(j)
            print(satirstringi)
            
            if karaktersayisi == sayi + 1:
                karaktersayisi = karaktersayisi - 1
                sınır = 1
            else:
                if sınır == 1:
                    karaktersayisi = karaktersayisi - 1
                else:
                    karaktersayisi = karaktersayisi + 1
    else:
        print(' 0-9 aralığı için bir sayı girmediniz.')
