#=============================================================================
# Bir listenin cift indexli elemanlarinin carpimini bulan algoritmayi
# fonksiyon seklinde kodlayiniz.
#=============================================================================
# HATA YA DA PERFORMANS DURUMLARI:
    # Liste elemanlarından bir tanesinin 0 olması
#=============================================================================
# Bu algoritma liste içerisinde sıfır sayısına denk gelirse çarpma işlemini
# sonlandırır. 
#=============================================================================
# NOT: Bu fonksiyona her zaman sayılardan oluşan bir liste aktarılacağı
# varsayılmıştır.

def ciftindex( liste ):
    
    es = len( liste )
    carpim = 1

    for i in range(0,es,2):
        if liste[i] == 0:
            return 0,sayici
        carpim = carpim * liste[i]

        
    return carpim,sayici
