def drugi_najvecji(s):
    slovar = {}
    for cifra in s:
        #print(cifra)
        if cifra not in slovar:
            slovar[cifra] = 1
        else:
            slovar[cifra] += 1
        
    max = -1000
    for kljuc, value in slovar.items():
        if max < kljuc:
            max = kljuc
    
    del slovar[max] #zbrise kljuc in vrednost iz slovarja tak je max

    maks = -1000
    for k, v in slovar.items():
        if maks < k:
            maks = k
    print(maks)
    
    #print(slovar)


    #print(slovar)
        




vrne = drugi_najvecji([9, 1, 4, 8, 2, 3, 8])
print(vrne)