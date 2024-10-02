def najmanjsi_unikat(s):
    slovar = {}
    for e in s:
        if e not in slovar:
            slovar[e] = 1
        else:
            slovar[e] += 1
    
    #return slovar
    for kljuc, vrednost in slovar.items():
        if vrednost == 1:
            unikat = kljuc
            return unikat
        if len(slovar) == 0:
            return None
    
    

vrne = najmanjsi_unikat([])
print(vrne)