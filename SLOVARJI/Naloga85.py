def zamenjano(s, menjave):
    nov_seznam =  []
    for ime in s:

        if ime in menjave:
            ime = menjave[ime]

        nov_seznam.append(ime)

    return(nov_seznam)




vrne = zamenjano(["Ana", "Ana", "Berta", "Ana", "Cilka"], {"Ana": "Peter", "Berta": "Ana"})
print(vrne)