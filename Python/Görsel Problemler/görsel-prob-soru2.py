#=================================================================
# Aşağıda yer alan yılın belli bir ayına ait takvimi çıktı olarak
# verecek algoritmayı fonksiyon şeklinde kodlayınız.

#       PZ    SL    ÇR    PR    CM    CMR    PZR    
#       ----------------------------------------
#        *     *     *     *     *     1     2
#        3     4     5     6     7     8     9
#       10    11    12    13    14    15    16
#       17    18    19    20    21    22    23
#       24    25    26    27    28    29    30
#       31     *     *     *     *     *     *

#=================================================================

# Takvim bir matris olarak düşünülmüş ve her bir satır gerekli
# şartlar altında dizilim listesinde oluşturulup ekrana basılmıştır.
# Algoritmada ufak iyileştirilmeler yapılabilir.

def takvimgoruntule():
    
    print('PZ    SL    ÇR    PR    CM    CMR    PZR  ')
    print('----------------------------------------')
    gun = 1
    for satir in range(0,6): 
        dizilim = ''
        for sutun in range(0,7): 
            
            if (satir == 0 and sutun <= 4) or ( satir == 5 and sutun >= 1):
                dizilim = dizilim + ' *' + '    '
            else:
                uzunluk = len( str(gun) )
                if uzunluk < 2:
                    dizilim = dizilim + ' ' + str(gun) + '    '
                    gun = gun + 1
                else:
                    dizilim = dizilim + str(gun) + '    '
                    gun = gun + 1
        print(dizilim)
        
        
        
        
        
        
