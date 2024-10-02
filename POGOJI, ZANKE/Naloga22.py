def poprecje(s):
    povprecna_teza = 0
    rezultat = 0
    for teza in s:
        if len(s) == 0:
            print(rezultat)
        else:
            povprecna_teza += teza
            rezultat = povprecna_teza / len(s)

    return rezultat

    #print(povprecna_teza) --> da preverim če pravilno izpisuje


vrne = poprecje([5, 8, 12])
print(vrne)
