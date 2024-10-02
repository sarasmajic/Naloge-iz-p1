podatki = [
    ["Ana", 55, 165],
    ["Berta", 60, 153],
]


indeks = 0
for seznam in podatki:
    ime = seznam[0]
                                        #print(seznam[1], seznam [2]) --> za delovanje
    teza = seznam[1]
    visina = (seznam[2] / 100)
                                        #print(teza) DELOVANJE
                                        #print(visina) DELOVANJE
    indeks =  teza // (visina ** 2)
    print(ime, indeks)
    #KAKO NAJ IZPIŠE ŠE OSEBO ZRAVEN

    