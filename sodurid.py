from oop_alused.sodur import Sodur

sodur 1 = Sodur()
sodur 2 = sodur()

while(sodur1.tervis > 0 and sodur2.tervis > 0):
    kes_loob = radint(1,2)
    if(kes_loob == 1)
        print("esimene lööb teist")
        sodur2.tervis -= 20
    if(kes_loob == 2):
        print("tenie lööb esimest")
        sodur1.tervis -= 20

    if sodur1.tervis != 0:
        print("teine sõdur voitis")

    else:
        print("esimene sõdur võitis")