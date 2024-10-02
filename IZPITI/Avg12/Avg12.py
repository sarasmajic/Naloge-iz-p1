#1 če se vsak znak v nizu pojavi natančno 2x
def vse_po_dvakrat(s):
    slovar = {}
    seznam = []

    for znak in s:
        if znak == " ":
            continue
        else:
            if znak not in slovar:
                slovar[znak] = 1
            else:
                slovar[znak] += 1
    
    for key, value in slovar.items():
        seznam.append(value)
    
    for i in range(len(seznam) - 1):
        if seznam[i] == seznam[i + 1]:
            continue
        else:
            return False
    return True     
    #print(slovar[znak])
vrne = vse_po_dvakrat("")
print(vrne)

print("---------")

#2 skupno besedo pretvori v dve, ki ju povezuje _, spremenjena navodila
def brez_grb(beseda):
    string = ""

    for crka in beseda:
        if crka.islower() == True:
            string += crka
        else:
            string += "_"
    
        if crka.isupper() == True:
            string += crka
    return(string)


vrne = brez_grb("kameljaImena")
print(vrne)

