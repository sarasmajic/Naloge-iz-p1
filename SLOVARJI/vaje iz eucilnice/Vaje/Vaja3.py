#Za vsako postajo zapiši največjo zabeleženo razliko med najnižjo in najvišjo temperaturo v istem dnevu.

razlike = {}

for vrstica in open("vremenske-postaje.txt"):
    kraj, datum, najvisja, najnizja = vrstica.split(",")
    najvisja = int(najvisja)
    najnizja = int(najnizja)
    razlika = najvisja - najnizja

    if kraj not in razlike or razlike[kraj] < razlika:
        razlike[kraj] = razlika #VALUESI NAJ SE NASTAVAIJO NA VREDNOST NAJVISJA


print(razlike)

