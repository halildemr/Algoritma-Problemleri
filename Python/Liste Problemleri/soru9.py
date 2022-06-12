#=============================================================================
# Bir listenin ortalamasini hesaplayan ve ortalamadan buyuk olan degerleri
# ekrana basan algoritmayi fonksiyon seklinde kodlayiniz.
# [125, 92, 5, 81, 21, 17, 32, 4, 0]
#=============================================================================
# Bu fonksiyona her zaman sayılardan oluşan bir listenin aktarılacağı 
# varsayılmıştır. Aksi halde 12. veya 16. veya 22. satırda hata verecektir. 
#=============================================================================
def listeOrtalama( liste ):
    
    uzunluk = len( liste )
    toplam = 0
    
    for i in range(0,uzunluk):
        toplam = toplam + liste[i]
        
    ortalama = toplam / uzunluk
    print('Ortalama...: ',ortalama)
    
    for j in range(0,uzunluk):
        if liste[j] > ortalama:
            print(liste[j])
