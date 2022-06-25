#=============================================================================
# Pascal üçgenini belirtilen satır sayısı kadar ekrana basan 
# algoritmayı kodlayınız. 
# Örnek: 
#       satırsayısı = 7
#       [1]
#       [1 1]
#       [1 2 1]
#       [1 3 3 1]
#       [1 4 6 4 1]
#       [1 5 10 10 5 1]
#       [1 6 15 20 15 6 1]
#       ...
# [ [1], [1,1] ]
#=============================================================================


def pascal( satirsayisi ):
    
    pascalucgeni = [ [1] , [1,1] ]

    x = 3
    while x <= satirsayisi:
        
        sonsatir = pascalucgeni[ len(pascalucgeni) - 1 ]
        sonsatirinElemanSayisi = len( sonsatir )
        
        yenisatir = [ 1 ]
        for j in range(0,sonsatirinElemanSayisi-1):
            toplam = sonsatir[j] + sonsatir[j+1]
            yenisatir.append( toplam )
        yenisatir.append( 1 )
        
        pascalucgeni.append( yenisatir )
        x = x + 1
        
    
    for k in range(0,len(pascalucgeni)):
        print(pascalucgeni[k])
