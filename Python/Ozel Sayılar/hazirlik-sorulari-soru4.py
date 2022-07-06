#=================================================================
# Pozitif bir sayının pozitif tam bölenlerinin toplamını tespit
# edecek algoritmayı kodlayınız.
# 8 sayısının pozitif tam bölenleri ---> 1,2,4,8 ---> 15
#=================================================================

def pozitifTamBolenToplami( p ):
    
    toplam = 0
    for i in range(1,p+1):
        if p % i == 0:
            toplam = toplam + i
            
    return toplam
  
  
  
