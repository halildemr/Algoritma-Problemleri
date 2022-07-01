#================================================================
# Bir bisiklet kiralama firması kiralama ücretini şöyle belirler:
# Her bir dakika için 0.50 Kuruş talep edilir. Fakat kullanım 
# süresinin farklı durumları için aşağıdaki koşullar uygulanır.

# dakika <= 30  dakika başı 0.50 kuruş

# dakika <= 60  
# ilk 30 dakika 0.50 kuruş, sonraki dakikaler için dakika başı 
# %5 indirim

# dakika > 60 ise
# ilk 30 dakika 0.50 kuruş
# ikinci 30 dakika %5 indirim
# 60'ın üzeri her dakika %25 indirim 

# 5 dakikadan önce getirilen bisikletler için kiralama ücreti 
# talep edilmez!
# BU ŞARTLARLA BERABER GİRİLECEK SÜRE BİLGİSİNE GÖRE
# KİRALAMA ÜCRETİNİ HESAPLAYAN ALGORİTMAYI KODLAYINIZ
#================================================================

def bisikletkiralamaucreti( kullanimsuresi ):
    
    dakikaucreti = 0.5
    
    if kullanimsuresi >= 5:
        
        if kullanimsuresi <= 30:
            tutar = kullanimsuresi * dakikaucreti
            print('Tutar....:',tutar)
            
        elif kullanimsuresi <= 60:
            tutar = 30*dakikaucreti + (kullanimsuresi - 30) * dakikaucreti *0.95
            print('Tutar...:',tutar)
            
        elif kullanimsuresi > 60:
            tutar = 30*dakikaucreti + 30*dakikaucreti*0.95 + (kullanimsuresi - 60 )*dakikaucreti*0.75
            print('Tutar.....:',tutar)
        
    else:
        print('Tutar....: 0TL')
        
