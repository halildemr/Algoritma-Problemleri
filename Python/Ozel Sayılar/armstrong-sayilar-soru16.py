#=================================================================
# Girilecek pozitif bir n tam sayının Armstrong sayı olup
# olmadığını tespit edecek python kodlarını yazınız.
#=================================================================

def armstrong( n ):
    
    stringsayi = str( n )
    uzunluk = len( stringsayi )
    toplam = 0 
    
    for i in range(0,uzunluk):
        rakam = int( stringsayi[i]) 
        toplam = toplam + rakam**3
        
    if toplam == n:
        print('Girilen sayı armstrong')
    else:
        print('Girilen sayı armstrong değil.')
        
        
        
        
