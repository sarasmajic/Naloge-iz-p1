def podobna(beseda):
    besede = ["ana", "berta", "cilka", "dani", "ema", "fanci", "greta", "hilda"]


    slovar_beseda = {}
    max_ujemanj = 0


    for crka in beseda:
        if crka not in slovar_beseda:
            slovar_beseda[crka] = 1


    for ime in besede:
        imena = {}  #za vsako besedo sem ustvarila slovar
        for crka in ime:
            if crka not in imena:
                imena[crka] = 1

    
        ujemanja = 0
        for crka in slovar_beseda:    #TREBA JE BILO ZAMAKNIT
            if crka in imena:
                ujemanja += 1
                #print(ujemanja, crka)
        
        if max_ujemanj < ujemanja:
            max_ujemanj = ujemanja
            iskana_beseda = ime
        
    print(iskana_beseda)
            

vrne = podobna("merjasec")
print(vrne)