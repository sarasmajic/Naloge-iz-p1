def ne_na_lihih(s):
    slovar = {}
    for i in range(len(s)):

        if s[i] not in slovar and i % 2 == 0:
            slovar[s[i]] = s[i]

    #for cifra in s:
        #print(cifra) -- vrne cifre
        #if cifra not in slovar and 

    print(slovar)



vrne = ne_na_lihih([12, 17, 17, 5, 3])
print(vrne)

#TREBA NAREST Z MNOZICAMI!!