def narocila(s):
    slovar = {}

    for terka in s:
        #print(terka[0]) -- vrne vsa imena
        ime = terka[0]
        narocilo = terka[1]
        #print(narocilo)
        if ime not in slovar:
            slovar[ime] = narocilo
        else:
            slovar[ime] += "haha"

    print(slovar)

vrne = narocila([("Ana","torta"),("Berta","krof"),("Cilka","kava"), ("Ana", "kava"), ("Berta", "-krof"), ("Cilka", "-torta"), ("Berta", "torta")])
print(vrne)