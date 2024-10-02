def racunaj(cene, nakupi):
    slovar = {}
    vsota = 0
    vsota_kup = 0

    for vrstica in open(cene):
        vrstica = vrstica.split(" ")
        cena = vrstica[1]

        cena = float(cena.strip())
        sifra_izd = int(vrstica[0])

        slovar[sifra_izd] = cena

        for vrs in open(nakupi):
            vrs = vrs.split(" ")
            sifra_izd_kupleno = int(vrs[0])

            kolicina = vrs[1]
            kolicina = float(kolicina.strip())

            if sifra_izd_kupleno == sifra_izd:
                print(slovar[sifra_izd])
                vsota = kolicina * slovar[sifra_izd]
    
                vsota_kup += vsota
    print(vsota_kup)
                 #vsota = kolicina * slovar[sifra_izd]
        
    #print(vsota)

    



vrne = racunaj("cene.txt", "nakupi.txt")
print(vrne)