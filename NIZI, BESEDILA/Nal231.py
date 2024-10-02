def beri_skupine(ime, ime_dat):
    slovar = {}
    seznam = []

    for vrstica in open(ime_dat):
        vrstica = vrstica.strip()
        vrstica = vrstica.split(":")
    
        vrednosti = (vrstica[-1])
        vrednosti = vrednosti.split(",") #seznam z imeni
        grupa = vrstica[0]

        slovar[grupa] = vrednosti
    
        if ime in slovar[grupa]:
            seznam.append(grupa)
 
    return seznam
    

    #if ime in slovar[grupa]:
     #   print(slovar[grupa])
    
    



     

vrne = beri_skupine("ana", "group.txt")
print(vrne)