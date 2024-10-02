def zdruzi(s):
    slovar = {}
    for i in range(len(s)):
        #s[i] -- cifre
        if s[i] not in slovar:
            slovar[s[i]] = set()  #množice
        slovar[s[i]].add(i)
    
    return slovar

vrne = zdruzi([3, 1, 12, 3, 7, 12])
print(vrne)


def razmeci(slo):
    for i, vre in slo.items():
        print(i, vre)

        #nenarjeneo




vrn = razmeci({3: {0, 3}, 1: {1}, 12: {2, 5}, 7: {4}})
print(vrn)