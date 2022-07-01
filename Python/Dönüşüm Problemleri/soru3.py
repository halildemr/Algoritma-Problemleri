#=================================================================
# 4 basamaklı sayıların Türkçe karşılıklarını oluşturan 
# dönüşüm algoritmasını kodlayınız.
#
# Girdi -->  1569 
# Çıktı -->  Bin Beş yüz Altmış Dokuz
#
# Girdi --> 1001
# Çıktı --> Bin Bir
#=================================================================

def sayilariTurkceyeDonustur( sayi ):
    
    binlerbasamagi = ['Bin','İki Bin','Üç Bin','Dört Bin','Beş Bin',
                      'Altı Bin','Yedi Bin','Sekiz Bin','Dokuz Bin']

    yuzlerbasamagi = ['Yüz','İki Yüz','Üç Yüz','Dört Yüz','Beş Yüz',
                      'Altı Yüz','Yedi Yüz','Sekiz Yüz','Dokuz Yüz']
    
    onlarbasamagi = ['On','Yirmi','Otuz','Kırk','Elli','Altmış','Yetmiş',
                     'Seksen','Doksan']
    
    birlerbasamagi = ['Bir','İki','Üç','Dört','Beş',
                      'Altı','Yedi','Sekiz','Dokuz']
    
    
    stringsayi = str( sayi )
    kelimeler = ''
    
    if stringsayi[0] != '0':
        index = int( stringsayi[0] ) - 1
        kelimeler = kelimeler + binlerbasamagi[ index ] + ' '
        
    if stringsayi[1] != '0':
        index = int( stringsayi[1] ) - 1
        kelimeler = kelimeler + yuzlerbasamagi[ index ] + ' '
        
    if stringsayi[2] != '0':
        index = int( stringsayi[2] ) - 1
        kelimeler = kelimeler + onlarbasamagi[ index ] + ' '
        
    if stringsayi[3] != '0':
        index = int( stringsayi[3] ) - 1
        kelimeler = kelimeler + birlerbasamagi[ index ] + ' '
        
    return kelimeler
  
  
  
  
  
  
  
