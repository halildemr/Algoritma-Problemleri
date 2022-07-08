#=================================================================
# 1-100 arasındaki yarı mükemmel sayilari tespit eden python 
# kodlarını yazınız.
#=================================================================

def yarimukemmel():
    
    for i in range(1,101):
        
        pb = []
        
        for j in range(1,i):
            if i % j == 0:
                pb.append(j)
                
        uzunluk = len( pb)
        if uzunluk > 3:
            toplam = pb[uzunluk-1] + pb[uzunluk-2] + pb[uzunluk-3]
            
            if toplam == i:
                print('Yarı mükemmel...: ',i)

