#=================================================================
# Bir sayıyı tersine çevirip yeni sayı elde eden algoritmayı 
# kodlayınız.
# 123456 ----> 654321
# 12023400 ---> 00432021 ---> 432021
#=================================================================
# Algoritma pozitif sayılar için çalışır
#=================================================================

def tersecevir( x ):
    
    stringsayi = str( x )
    terssayi = ''
    
    for i in range( len(stringsayi)-1,-1,-1):
        terssayi = terssayi + stringsayi[i]
        
    if terssayi[0] == '0':
        for j in range(0,len(terssayi)):
            if terssayi[j] != '0':
                index = j
                break
            
        yeniterssayi = ''
        for k in range(index,len(terssayi)):
            yeniterssayi = yeniterssayi + terssayi[k]
            
        return int(yeniterssayi)
    else:
        return int(terssayi)
