def naslednji_avtobus(prihodi):
    seznam = []
    min = 1000
    min_bus = 10000

    for kljuc in prihodi:  #kljuc je 1, 3, 6b
    
        for vrednost in prihodi[kljuc]:
            if vrednost < min:
                min = vrednost
                bus = kljuc
    
    seznam.append(bus)

    if min in prihodi[kljuc]:
        seznam.append(kljuc)

    
    for e in seznam:
        if e.isnumeric():
            e = int(e)
        else:
            if len(e) > 1:
                e = int(e[:-1])
       
        
        if e < min_bus:
            min_bus = e
    
    return(min_bus)
        
vrne = naslednji_avtobus({"1": [5, 7], "2": [11, 3, 18], "11": [3, 7]})
print(vrne)