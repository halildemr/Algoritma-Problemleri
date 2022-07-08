#=================================================================
# 1-100 arasındaki mükemmel sayıları tespit eden python kodlarını
# yazınız.
#=================================================================

def mukemmel():
    
    for i in range(1,500):
        
        toplam = 0
        
        for j in range(1,i):
            if i % j == 0:
                toplam = toplam + j
                
        if toplam == i:
            print('MÃ¼kemmel sayÄ±...: ',i)
