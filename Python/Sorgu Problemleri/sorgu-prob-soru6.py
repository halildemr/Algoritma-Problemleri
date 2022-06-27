#================================================================
# Girilen ay sayısına göre ilgili ayın kaç günden oluştuğunu
# söyleyen algoritmayı kodlayınız.
# [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#================================================================


def ayingunsayisiniver( ay ):
    
    if ay == 1 or ay == 3 or ay == 5 or ay == 7 or ay == 8 or ay == 10 or ay == 12:
        print('31 Gün')
    elif ay == 2:
        print('29 Gün')
    elif ay == 4 or ay == 6 or ay == 9 or ay == 11:
        print('30 Gün')
        
