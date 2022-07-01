#=================================================================
# Santimetre/Metre, Metre/Santimetre Dönüşümünü uygulayan 
# algoritmayı kodlayınız
#
# Girdi -->  1 , 'cm' (1 metreyi santimetreye çevir)
# Çıktı -->  100
#
# Girdi -->  1 , 'm' (1 santimi metreye çevir)
# Çıktı -->  0,01
#
# Girdi -->  0.99 , 'm' (0.99 santimi metreye çevir)
# Çıktı -->  99.0 
#=================================================================



def uzunlukD( uzunluk, uzunlukbirimi ):
    
    santimetre = 100
    
    if uzunlukbirimi == 'cm':
        sonuc = uzunluk / santimetre
        print(str(uzunluk)+' santimetre '+str(sonuc) + ' metredir.')
    elif uzunlukbirimi == 'm':
        sonuc = uzunluk * santimetre
        print(str(uzunluk)+' metre '+str(sonuc) + ' santimetre.')
        
