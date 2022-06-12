#=============================================================================
# Fonksiyona aktarilacak liste ve index numarasina gore listeyi
# iki parcaya ayiran ve bunlari konsola cikti olarak veren
# algoritmayi fonksiyon şeklinde kodlayiniz.

# [9753]
# [125, 92, -5, 81, 21, 17, 32, 4, 0] , 2
#=============================================================================

def ikiyeparcala( liste, index ):
    
    elemansayisi = len( liste )
    if elemansayisi > 1:
        if index >= 0 and index <= elemansayisi - 1:
            parca1 = []
            parca2 = []
            
            for i in range(0,index+1):
                parca1.append( liste[i] )
            for j in range(index+1, elemansayisi):
                parca2.append( liste[j] )
            
            print(parca1)
            print(parca2)
        
        else:
             print("index liste sınırını aştı.")
    else:
        print('Bu liste parçalanamaz.')
        print(liste)
