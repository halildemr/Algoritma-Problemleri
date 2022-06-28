#=================================================================
# 1 ile 10 arasında girilecek pozitif bir tam sayı için aşağıdaki
# şekilde çıktı üreten algoritmayı fonksiyon şeklinde kodlayınız.
# Girdi --> 3
# Çıktı --> 
#                 ....     
#                 .  .     
#                 ....    
#=================================================================

def dikdortgenciz( sayi ):
  
    if type(sayi) == int:
      
        if sayi >= 1 and sayi <= 10:
          
            if sayi == 1:
                print('.')
            else:
                print( sayi * '.' )
                for i in range(0,sayi-2):
                    print('.' + (sayi-2) * ' ' + '.')
                print( sayi * '.')
            
        else:
            print(' 1-10 aralığında bir sayı girmediniz.')
    else:
        print("Tam sayı girmediniz!")
        
