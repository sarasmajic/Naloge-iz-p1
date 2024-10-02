ponudbe = []

for vrstica in open("zapisnik-analiza.txt"):
    predmet, oseba, cena = vrstica.split(",")
    cena = int(cena)
    ponudbe.append([predmet, oseba, cena]) #en seznam, podatki predmet, oseba, cena so notr

predmeti_s_cenami = {}

for predmet, _, cena in ponudbe: #_ je za osebo --> to če ne rabiš
    if predmet not in predmeti_s_cenami:
        predmeti_s_cenami[predmet] = []
    predmeti_s_cenami[predmet].append(cena)

for predmet in predmeti_s_cenami:

    if len(predmeti_s_cenami[predmet]) < 7:
        razlika = max(predmeti_s_cenami[predmet]) - min(predmeti_s_cenami[predmet])
    else:
        razlika= predmeti_s_cenami[predmet][-1] - predmeti_s_cenami[predmet][-7]
    
    print(predmet, "-", razlika) #znotraj loopa razlike ker rabimo za usak predmet

# seznam[4] -> peti elememt seznama
# seznam[-1] -> zadnji element seznama

# len(seznam) -> dolzina seznama