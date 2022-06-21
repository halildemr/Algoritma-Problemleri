#=============================================================================
# Bir karakter toplulugunda gecen x karakterinin sayisini ve adres bilgilerini
# veren algoritmayi fonksiyon seklinde kodlayınız.
# Not: Karakter topluluğundan kasıt bir stringtir.
#=============================================================================
# Fonksiyonun c parametresine int, float gibi ilkel veri tipleri gönderilirse
# 15. satırda hata oluşur.
#=============================================================================

cumle = """Bir karakter topluluğunda geçen x karakterinin sayısını ve 
adres bilgilerini veren algoritmayı kodlayınız."""

def arastir( c, x = ' '):
    
    karaktersayisi = len( c )
    adresler = []
    sayici = 0
    
    for i in range(0,karaktersayisi):
        if c[i] == x:
            sayici = sayici + 1 
            adresler.append( i )
            
    return adresler,sayici
