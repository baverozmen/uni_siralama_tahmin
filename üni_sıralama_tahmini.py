
import time

import pywhatkit

while True:
    print("çıkmak için: 0")

    print("""1 yıllık veri için: 1""")

    print("2 yılık veri için: 2 ")

    print("3 yıllık veri için: 3")

    print("4 yıllık veri için: 4")

    print("mesaj göndermek için : 5")

    time.sleep(2)

    def sonucx(toplam : int,bölünen: int):
        return 1 + (toplam/bölünen)





    choose = int(input("lütfen seçiniz: "))

    if choose == 0:
        print("çıkış yapıldı")
        break

    elif choose == 1:
        oneYear = int(input("degeri giriniz (2023): "))
        #nameCateg = str(input("lütfen bölüm adını giriniz: "))
        time.sleep(2)

        print("bekleyiniz...")
        time.sleep(3)

        print("birazdan getirilen siteye girip istediginiz bölümün farklı üniversitedeki 4 yıllık verilerini yüzde hesaplama bölümüne girin... ")
        time.sleep(2)
        print("https://yokatlas.yok.gov.tr/lisans-anasayfa.php")
        time.sleep(2)




        yzde = input("yüzde hesaplamak ister misiniz (y/n): ")

        if yzde == "y":
            fourYear4 = int(input("1. degeri giriniz(2023): "))
            fourYear5 = int(input("2. degeri giriniz(2022): "))
            fourYear6 = int(input("3. degeri giriniz(2021): "))
            fourYear7 = int(input("4. degeri giriniz(2020): "))

            sonuc = (((fourYear4 - fourYear5)/fourYear5) + ((fourYear5-fourYear6)/fourYear6) + ((fourYear6 - fourYear7)/fourYear7))
            print(f"2024 tahmini sıralaması :{oneYear * ( sonucx(sonuc, 3))}")

            print("bu sonuc eldeki az veriden dolayı olasılık olarak düşüktür")
            time.sleep(4)
        else:
            print("basa dönebilirsiniz")


    elif choose == 2:
        twoYear = int(input("1. degeri giriniz(2023): "))

        twoYear_1 = int(input("2. degeri giriniz(2022): "))
        time.sleep(2)
        print("hesaplanıyor...")
        time.sleep(2)
        sonuc_1 = ((twoYear - twoYear_1) / twoYear_1)
        print(f"2024 tahmini sıralaması :{twoYear * ( sonucx(sonuc_1,1))}")



    elif choose == 3:
        threeYear = int(input("1. degeri giriniz(2023): "))
        threeYear_2 = int(input("2. degeri giriniz(2022): "))
        threeYear_3 = int(input("3. degeri giriniz(2021): "))
        time.sleep(2)
        print("hesaplanıyor...")
        time.sleep(2)
        sonuc_2 = (((threeYear_2 - threeYear_3) / threeYear_3) + ((threeYear - threeYear_2) / threeYear_2))
        print(f"2024 tahmini sıralaması :{threeYear * (sonucx(sonuc_2, 2))}")


    elif choose == 4:
        fourYear = int(input("1. degeri giriniz(2023): "))
        fourYear_1 = int(input("2. degeri giriniz(2022): "))
        fourYear_2 =  int(input("3. degeri giriniz(2021): "))
        fourYear_3 =  int(input("4. degeri giriniz(2020): "))
        time.sleep(2)
        print("hesaplanıyor...")
        time.sleep(2)

        sonuc_3 = (((fourYear- fourYear_1) / fourYear_1) + ((fourYear_1 - fourYear_2) / fourYear_2) + ((fourYear_2 - fourYear_3) / fourYear_3))
        print(f"2024 tahmini sıralaması :{fourYear * (sonucx(sonuc_3, 3))}")

    elif choose == 5:
        try:
            telNum = input("göndereceginiz kişinin telefon numarası(ülke kodunu giriniz): ")
            msg_send = input("buldunuguz sonuç: ")
            time_h = int(input("göndereceginiz saati seçin: "))
            min_h = int(input("göndereceginiz dakikayı seçin: "))
            pywhatkit.sendwhatmsg(telNum,msg_send,time_h, min_h)
        except:
            print("hatalı işlem oldu")

    else:
        print("lütfen seçimi dogru yapın")
