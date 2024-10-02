seznam = []
slovar = {}
razlika = 0

for vrstica in open("zapisnik.txt"):
    predmet, oseba, cena = vrstica.split(",")
    cena = int(cena)
    seznam.append([predmet, oseba, cena])  #lahko naredis tut predmeet, oseba,cena = vrstica.split
                            #seznam.append([predmet, oseba, cena])


for sez in seznam:
    if sez[0] not in slovar:
        slovar[sez[0]] = [sez[2]]
    else:
        slovar[sez[0]].append(sez[2])



for kljuc, value in slovar.items():
    if len(value) < 7:
        razlika = value[-1] - value[0]
    else:
        razlika = value[-1] - value[-7]

    print(kljuc , " - ", razlika)





