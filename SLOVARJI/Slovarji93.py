def kronogrami(niz):
    slovar = {}
    for crka in niz:

        if crka == "I":
            if crka not in slovar:
                slovar[crka] = 1
            else: 
                slovar[crka] += 1

        if crka == "V":
            if crka not in slovar:
                slovar[crka] = 5
            else:
                slovar[crka] = 5

        if crka == "X":
            if crka not in slovar:
                slovar[crka] = 10
            else:
                slovar[crka] = 10

        if crka == "L":
            if crka not in slovar:
                slovar[crka] = 50
            else:
                slovar[crka] = 50

        if crka == "C":
            if crka not in slovar:
                slovar[crka] = 100
            else:
                slovar[crka] = 100

        if crka == "M":
            if crka not in slovar:
                slovar[crka] = 1000
            else:
                slovar[crka] = 1000
        
        
        #slovar[crka] = 1
    
    #print(slovar)

    vrednost = 0
    for kljuc, value in slovar.items():
        #print(value)
        vrednost += value

    print(vrednost)


vrne = kronogrami("CVIVS IN HOC RENOVATA LOCO PIA FVLGET IMAGO SIS CVSTOS POPVLI SANCTE IACOBE TVI")
print(vrne)