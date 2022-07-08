#=================================================================
# 37. fibonacci sayisini tespit eden algoritmayı kodlayınız.
#=================================================================


def fibo37():
    
    birincisayi = 1
    ikincisayi = 1
    fibonaccisayisi = 2
    
    while True:
        sonrakisayi = birincisayi + ikincisayi
        birincisayi = ikincisayi
        ikincisayi = sonrakisayi
        
        fibonaccisayisi = fibonaccisayisi + 1
        
        if fibonaccisayisi == 37:
            print(sonrakisayi)
            break
