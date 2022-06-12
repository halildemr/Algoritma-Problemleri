#=============================================================================
# Bir listenin herhangi bir elemanini klavyeden alinan
# deger ve index numarasi ile degistiren algoritmayi kodlayiniz.
# Koşul: belirtilen indexe sadece sayı aktarılabilir.
# [125, 92, -5, 81, 21, 17, 32, 4, 0], 3, 91753

# HATA DURUMLARI:
    # Liste sınırını aşan index belirtilmesi
    # Fonksiyonun "liste" parametresine gönderilen int, float vb.
#=============================================================================

def listeElemanDegistir( liste, index, eleman ):
    
    if type(liste) == list:
        es = len( liste )
        if index >= 0 and index <= es -1:
            if type(eleman) == int or type(eleman) == float:
                liste[index] = eleman
                print(liste)
            else:
                print('Listeye sadece sayı eklenebilir')
        else:
            print('İndex liste sınırını aştı.')
    else:
        print('Veri tipi hatası: \n İlk parametre bir liste olmaldıdır.')
