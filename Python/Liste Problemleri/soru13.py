#=============================================================================
# Bir listedeki tek ve cift sayilari tespit ediniz ve bunları farklı 
# listelere kayit ederek konsolda görüntüleyiniz.
#=============================================================================

sayilar = [1,2,3,4,5,6,10,25,16,95,12,63,75,18,94,102,34,561,2,3,8,7,94,61]

def tekciftAyristir( liste ):
    
    es = len( liste )
    teksayilar = []
    ciftsayilar = []
    
    for i in range(0,es):
        if liste[i] % 2 == 1:
            teksayilar.append( liste[i] )
        else:
            ciftsayilar.append( liste[i])
            
    print(teksayilar)
    print(ciftsayilar)
