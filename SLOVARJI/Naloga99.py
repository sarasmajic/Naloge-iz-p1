def vsi_deli(skatla, potrebno):
    for kljuc, vrednost in skatla.items():
        for key, value in potrebno.items():
            if kljuc == key:
                #print(kljuc) PRINTA AC
                if value <= vrednost:
                    continue
                else:
                    return False
                
    return True

vrne = vsi_deli({"A": 5, "B": 1}, {"A": 5, "B": 2})
print(vrne)


def kaj_manjka(skatla, potrebno):
    slovar_manjka = {}
    

    for kljuc, vrednost in skatla.items():
        for key, value in potrebno.items():

            if vsi_deli(skatla, potrebno) == False:
                if key not in skatla:
                    slovar_manjka[key] = value

                razlika = 0
                if key == kljuc:
                    if potrebno[key] > skatla[kljuc]:
                        razlika = value - vrednost
                        if razlika > 0:
                        #print(key)
                            slovar_manjka[kljuc] = razlika
                    #iskan_kljuc = key
                
                #3- 4 = -1
                #3- 3 = 0
                #3 - 2 = 1

    
    print(slovar_manjka)



vrn = kaj_manjka({"A": 2, "B": 1, "C": 3}, {"A": 3, "C": 2, "D": 2})
print(vrn)