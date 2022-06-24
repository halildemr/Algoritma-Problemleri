#=============================================================================
# Bir listenin en büyük ve en küçük elemanları arasındaki bütün değerlerin
# toplamını bulan algoritmayı fonksiyon şeklinde kodlayınız.
# []
# [1]
# [1,2] [1,1]
# [-5, 2, 2, 2, 2, 2, 2, 125, 4, 0] 0,7
# [125, 2, 2, 2, 2, 2, 2, -5, 4, 0] 7,0
# [2, 2, 2, 2, 2, 2, 125, -5, 4, 0] 7,6
#=============================================================================
# Problemin çözümü üç aşamadan oluşur:
# Listenin en büyük ve en küçük elemanlarının indexlerini tespit et.
# İndexleri küçükten büyüğe olacak şekilde diz.
# Eldeki indexlerleri kullanarak soldan sağa doğru listeyi oku ve toplamları bul.
#=============================================================================
# Olası liste durumları ve çözümleri:
# 0 elemanlı liste ---> işlem yapılmaz
# 1 elemanlı liste ---> işlem yapılmaz
# 2 elemanlı liste ---> en büyük en küçük eleman olsa bile arasında sayı yoktur
# bu nedenle işlem yapılmaz.
# 3 ve daha dazla elemana sahip listelerde alt durumlar mevcuttur. Bunları
# ilgili arkadaşlara bırakıyorum.

def indexliToplam( liste ):
    
    sonuc = enbuyukEnkucuk( liste )
    
    if sonuc == 0:
        print('Liste en az 3 elemanlı olmalıdır.')
        return
    
    index1 = sonuc[0]
    index2 = sonuc[1]
    toplam = 0
    
    for i in range(index1+1,index2):
        toplam = toplam + liste[i]
        
    print('Toplam....:',toplam)
    

        
def enbuyukEnkucuk( L ):
    
    es = len( L )
    
    if es > 2:
        index1 = 0
        index2 = 0
        
        for i in range(1,es):
            if L[i] < L[index1]:
                index1 = i
            if L[i] > L[index2]:
                index2 = i 
        
        return yerdegistir(index1,index2)
    else:
        return 0
    
    
    
def yerdegistir( index1 , index2 ):
    
    if index1 < index2:
        return index1,index2
    else:
        gecici = index1 
        index1 = index2
        index2 = gecici
        return index1,index2
      
      
      
      
