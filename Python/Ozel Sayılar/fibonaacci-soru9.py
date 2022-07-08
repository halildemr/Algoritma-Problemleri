#=================================================================
# ilk n adet fibonacci sayisini konsola cikti olarak veren
# python kadlarini yaziniz.
# Fibonacci dizisinin ilk 11 terimi
# 1,1,2,3,5,8,13,21,34,55,89 ...
#=================================================================

def ntaneFibo( n ):
    
    birincisayi = 1
    ikincisayi = 1
    print(birincisayi)
    print(ikincisayi)
    
    
    for i in range(3,n+1):
        sonrakisayi = birincisayi + ikincisayi
        birincisayi = ikincisayi
        ikincisayi = sonrakisayi
        print(sonrakisayi)
