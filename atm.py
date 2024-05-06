print("---------------------------------------")
print("<> ATM'YE HOŞGELDİNİZ <>")
print("--İŞLEMLER--")
print("""
*** 1. Bakiye sorgulama ***
*** 2. Para yatırma ***
*** 3. Para çekme *** 
*** 4. Kredi çekme ***
*** 5. Kredi ödeme ***
*** 6. Kredi borcu görme ***
** ATM'den çıkmak için "q" ya basın. **
""")      
print("---------------------------------------")

bakiye = 1000
banka_bakiyesi = 10000
kredi_borcu = 0

while True:
    islem = input("--İŞLEM SEÇİNİZ--> ")
    
    if (islem == "q"):
        print("Yine bekleriz.")
        break
    
    elif (islem == "1"):
        print("Güncel Bakiyeniz: ", bakiye)
        
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz miktarı girin: "))
        bakiye += miktar
        
    elif (islem == "3"):
        miktar1 = int(input("Çekmek istediğiniz miktarı girin: "))
        if (bakiye - miktar1 < 0):
            print("Yetersiz Bakiye...")
        else:
            bakiye -= miktar1
            
    elif (islem == "4"):
        cekme = int(input("Ne kadar kredi çekmek istersiniz: "))
        if (banka_bakiyesi - cekme < 0):
            print("Kredi çekme limitini aşan miktar girdiniz.")
        else:
            bakiye += cekme
            banka_bakiyesi -= cekme
            kredi_borcu += cekme
        
    elif (islem == "5"):
        print("Borcunuzu nakit veya banka bakiyenizden ödeyebilirsiniz.")
        odeme_turu = input("Ödeme türünü seçiniz (nakit / bakiye): ")
        if (odeme_turu == "nakit"):
            odeme_miktari = int(input("Ne kadar kredi ödemek istersiniz: "))
            if (odeme_miktari > kredi_borcu):
                print("Girdiğiniz miktar, kredi borcunuzdan fazla.")
            else:
                kredi_borcu -= odeme_miktari
        elif (odeme_turu == "bakiye"):
            odeme_miktari = int(input("Ne kadar kredi ödemek istersiniz: "))
            if (odeme_miktari > bakiye):
                print("Banka bakiyeniz yetersiz.")
            elif (odeme_miktari > kredi_borcu):
                print("Girdiğiniz miktar, kredi borcunuzdan fazla.")
            else:
                bakiye -= odeme_miktari
                kredi_borcu -= odeme_miktari
        else:
            print("Geçersiz ödeme türü.")
        
    elif (islem == "6"):
        print("Kredi kartı borcunuz:", kredi_borcu)
        
    else:
        print("Geçersiz İşlem...")

