#=================================================================
# Konsol ekranında isim ve yaş bilgilerinin düzenli şekilde
# görüntülenmesi istenmektedir. Kisileri görsel 2 de olduğu
# gibi düzenli şekilde görüntüleyen algoritmayı kodlayınız.

# GÖRSEL 1                GÖRSEL 2       
#=================================================================
# Ayşe: 25                Ayşe.......: 25
# Fatih: 23               Fatih......: 23 
# Kurtuluş: 25            Kurtuluş...: 25
# Hacivat: 32             Hacivat....: 32
# Karagöz: 30             Karagöz....: 30 
# Şinasi: 22              Şinasi.....: 22
#=================================================================

kisiler = {'Ayse':25,  'Fatih':23,  'Kurtuluş':25,   'Hacivat':32,
           'Karagöz':30,   'Şinasi':22}


def duzenliGoruntule( veri ):
    enbuyuk = 'Ayse'
    for key,yas in veri.items():
        if len(key) > len( enbuyuk ):
            enbuyuk = key
    toplamuzunluk = len( enbuyuk ) + 3
    
    for key,yas in veri.items():
        noktasayisi = toplamuzunluk - len(key)
        noktalar = noktasayisi*'.'
        print(key + noktalar + ': ',str(yas))
        
        
        
        
        
        
        
