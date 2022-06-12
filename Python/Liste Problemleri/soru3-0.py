#=============================================================================
# Bir listenin cift indexlerindeki elemanlarinin carpimini bulan algoritmayi
# fonksiyon seklinde kodlayiniz.
# [1,0,1,0,1,0,1,0,1,0]

# HATA YA DA PERFORMANS DURUMLARI:
    # Liste elemanlarından bir tanesinin 0 olması
#=============================================================================

def ciftindex( liste ):
    
    es = len( liste )
    carpim = 1
    
    for i in range(0,es,2):
        carpim = carpim * liste[i]
        
    return carpim
