def prafaktorji(n):
    slovar = {}
    while n > 1:
        for i in range(n):
            if n % (i + 1) == 0:
                if (i + 1) == 1:
                    continue
                else: 
                    n = n // (i + 1)
                    if (i + 1) not in slovar:
                        slovar[i + 1] = 1
                    else:
                        slovar[i + 1] += 1 
                    print(i + 1)
                    break
        
    return slovar



vrne = prafaktorji(1400)
print(vrne)

def gcd(a,b):
    zmnozek = 1
    for kljuc, vrednost in a.items():
        #print(kljuc)
        for key, value in b.items():
            if kljuc in b:
                if kljuc == key:
                    if a[kljuc] > b[key]:
                        min_vrednost = b[key]
                    else:
                        min_vrednost = a[kljuc]

                    n = kljuc ** min_vrednost
                    zmnozek = zmnozek * n
    return zmnozek


vrne = gcd({2: 3, 5: 2, 7: 1}, {2: 2, 7: 2, 11:1})
print(vrne)