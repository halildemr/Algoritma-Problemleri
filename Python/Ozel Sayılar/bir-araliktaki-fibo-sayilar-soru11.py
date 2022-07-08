#=================================================================
# Bir aralıktaki fibonacci dizisini veren python kodlarını
# yazınız.
# 1,1,2,3,5,8,13,21,34,55,89
# 1 2 3 4 5 6  7  8  9 10 11
#=================================================================


def aralikFibo(n,m):
    
    birincisayi,ikincisayi = ikiFiboGonder(n)
    
    for i in range(n,m+1):
        sonrakisayi = birincisayi + ikincisayi
        birincisayi = ikincisayi
        ikincisayi = sonrakisayi
        print(str(i) + '. fibo...: ',sonrakisayi)
    
    
def ikiFiboGonder(n):
    
    s1 = 1
    s2 = 1
    
    for i in range(3,n):
        sonraki = s1 + s2
        s1 = s2
        s2 = sonraki
        
    return s1,s2
