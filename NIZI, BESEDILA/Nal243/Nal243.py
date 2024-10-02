def migracije(ime_datoteke):
    slovar = {}
    slovar2 = {}
    max = -100

    for vrstica in open(ime_datoteke):
        vrstica = vrstica.split(":")
        stevilka = int(vrstica[0])
 
        lokacija = vrstica[1]
        lokacija = lokacija.strip()
        lokacija = lokacija.split("->")
        
    
        for e in lokacija:
            if e not in slovar:
                slovar[e] = stevilka
            else:
                slovar[e] += stevilka
    
    #print(slovar)

    for key, value in slovar.items():
        if value > max:
            max = value
            mesto = str(key)
    
    print(mesto)
        
        #print(stevilka, lokacija)
vrne = migracije("migracije.txt")
print(vrne)