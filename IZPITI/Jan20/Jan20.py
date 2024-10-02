def vrstni_red(ime_datoteke):
    #seznam = []
    slovar = {}

    for vrstica in open(ime_datoteke):
        vrstica = vrstica.split(":")
        ime = vrstica[0]
        minuta = int(vrstica[1])
        sekunda = int(vrstica[2])

        cas_v_sek = (minuta * 60) + sekunda
        
        slovar[ime] = cas_v_sek
    
    return slovar



vrne = vrstni_red("f1.txt")
print(vrne)

#1 nedokoncana in nepravilna
def brisi_ponovitve(s):
    slovar = {}

    for i,e in enumerate(s):
        if e not in slovar:
            slovar[e] = 1
        else:
            slovar[e] += 1

        if slovar[e] <= e:
            continue
        else:
            s.pop(i)
            i -= 1
    print(s)

vrne = brisi_ponovitve([1, 3, 4, 1, 3, 2, 2, 3, 5, 3, 2, 3, 4])
print(vrne)

#2
def najvecji_v_vseh(s):
    slovar = {}
    velikost_sez = len(s)  
    seznam_skupnih = []                    

    for seznam in s:
        for cifra in seznam:
            if cifra not in slovar:
                slovar[cifra] = 1
            else:
                slovar[cifra] += 1

            if slovar[cifra] == velikost_sez:
                seznam_skupnih.append(cifra)

    max = -1000
    if len(seznam_skupnih) == 0:
        return None
    else:
        for st in seznam_skupnih:
            if max < st:
                max = st
    
    return max
        
    #print(seznam_skupnih)

vrne = najvecji_v_vseh([[5, 1, 2, 3], [3, 1, 8], [42, 5, 3, 1]])
print(vrne)