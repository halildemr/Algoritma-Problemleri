#=================================================================
# ilk n tane tribonacci sayilarini tespit eden python kodlarini
# yaziniz.
# Tribonacci dizisinin ilk 11 terimi
# 1,1,2,4,7,13,24,44,81,149,274
#=================================================================

def ntaneTribo( n ):
    
    birincisayi = 1
    ikincisayi = 1
    ucuncusayi = 2
    print(birincisayi)
    print(ikincisayi)
    print(ucuncusayi)
    
    for i in range(3,n+1):
        sonrakiterim = birincisayi + ikincisayi + ucuncusayi
        birincisayi = ikincisayi
        ikincisayi = ucuncusayi
        ucuncusayi = sonrakiterim
        
        print(sonrakiterim)
        
