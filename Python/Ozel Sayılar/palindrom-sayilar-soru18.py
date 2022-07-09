#=================================================================
# Girilecek n m sayıları için n,m aralığında ki Palidrom sayıları
# tespit edecek python kodlarını yazınız. n,m pozitif tam sayı
#=================================================================


def palindrom( n,m ):
    
    if n > 0 and m > 0:
        for i in range(n,m+1):
            sayi = tersecevir( i )
            if sayi == i:
                print(i)
                
def tersecevir( x ):
    
    stringsayi = str( x )
    for i in range(len(stringsayi)-1,-1,-1):
        if stringsayi[i] != '0':
            index = i
            break
        
    terssayi = ''
    for j in range(index,-1,-1):
        terssayi = terssayi + stringsayi[j]
        
    return int(terssayi)
