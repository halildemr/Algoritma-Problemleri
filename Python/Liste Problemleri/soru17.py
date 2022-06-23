#=============================================================================
# Bir index numarasına göre bir listedeki komşu sayıların toplamını bulan 
# algoritmayı fonksiyon şeklinde kodlayınız.
# [ 1 ]
# [ 1,2 ]
# [ 1,2,3,4 ]
# A = [ 1,-12,1,-7,-27,25,42,51,53,3 ]
# A listesi için 2 indexi gidirilirse komşu sayılar [-12, -7] şeklindedir.
#=============================================================================
# Fonksiyona aktarılan listenin eleman sayısı bu problemin çözümünde 
# dikkate alınacak önemli bir noktadır. Öyle ki 0 ve 1 elemanlı listelerde 
# komşu sayılar bulunamaz. 2 elemanlı listelerde seçilen indexe göre her zaman
# 1 komşu bulunur. Eleman sayısı 2'den büyük listeler için komşu sayılar her zaman
# mevcuttur. Fakat burada girilen indexe göre komşu sayılar 1 ya da 2 tane olabilir
#=============================================================================
def komsusayilar( liste, index ):
    
    es = len( liste )
    
    if index >= 0 and index <= es - 1:
        
        if es == 1:
            print("komşu sayı yok.")
        else:
            if index == 0:
                toplam = liste[index + 1]
                print(toplam)
            elif index == es - 1:
                toplam = liste[index - 1]
                print(toplam)
            else:
                toplam = liste[index - 1 ] + liste[index + 1 ]
                print(toplam)
    else:
        print('İndex liste sınırını aştı.')
