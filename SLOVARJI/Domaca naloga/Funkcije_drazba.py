#družabno omrežje dražbe

#1
# Napiši funkcijo unikati(s), ki prejme seznam in vrne seznam, ki vsebuje iste elemente kot s, v enakem vrstnem redu, vendar brez ponovitev. Funkcija ne sme spreminjati podanega seznama, temveč mora vrniti novega.
def unikati(s):
    seznam = []

    for ime in s:
        if ime not in seznam:
            seznam.append(ime)
        else:
            continue
    return seznam

vrne = unikati(["Ana", "Ana", "Berta", "Cilka", "Ana", "Berta", "Berta", "Berta", "Ema", "Dani", "Cilka"])
print(vrne)

#2
def skupnih(s, t):
    seznam = []

    for ime in s:
        if ime in t:
            if ime not in seznam:
                seznam.append(ime)
            else:
                continue
    
    return (len(seznam))

vrne = skupnih(["Ana", "Berta", "Ana", "Ana", "Cilka"], ["Cilka", "Dani", "Ana", "Ana"])
print(vrne)

#3
def vseh(s, t):
    seznam = []

    for ime in s:
        if ime not in seznam:
            seznam.append(ime)
    
    for ime2 in t:
        if ime2 not in seznam:
            seznam.append(ime)
    
    return len(seznam)



vrne = vseh(["Ana", "Berta", "Ana", "Ana", "Cilka"], ["Cilka", "Dani", "Ana", "Ana"])
print(vrne)

#PROCESIRANJE SEZNAMOV
#1
def preberi_datoteko(ime_dat, locilo):
    seznam = []
    for vrstica in open(ime_dat):
        vrstica = vrstica.split(locilo)
        seznam.append(vrstica)
    return seznam

vrne = preberi_datoteko("kolesa.txt", "-")
print(vrne)


print("--------------------")
s = [["Ana", 5, 9, "Berta"],
     ["Cilka", 5, 12, "Berta"],
     ["Ana", 5, 9, "Cilka"],
     ["Berta", 5, 1, "Ana"]]
#2
def filtriran(s, stolpec, vrednosti):
    seznam = []
    for vrstica in s:
        if vrstica[stolpec] == vrednosti:
            seznam.append(vrstica)
    return seznam

vrne = filtriran(s, 1, "Ana")
print(vrne)

#3
print(".................")
def izlusci(s, stolpec):
    seznam = []
    for vrstica in s:
        seznam.append(vrstica[stolpec])
    return seznam

vrne = izlusci(s, 3)
print(vrne)

print()
#DRAŽBA
#1
def predmeti(ime_dat, oseba):
    seznam = []

    for vrstica in open(ime_dat):
        vrstica = vrstica.split(",")
        if oseba in vrstica:
            seznam.append(vrstica[0])

    return seznam
    
vrne = predmeti("drazba.txt", "Ana")
print(vrne)

print()

#2
def osebe(ime_dat,predmet):
    seznam = []

    for vrstica in open(ime_dat):
        vrstica = vrstica.split(",")
        if predmet in vrstica:
            seznam.append(vrstica[1])
    return seznam


vrne = osebe("drazba.txt", "slika")
print(vrne)

print("//////")

#3
def podobnost_oseb(ime_dat, oseba1, oseba2):
    seznam1 = []
    seznam2 = []

    sez = []
    sez_vse = []

    povprecje = 0

    for vrstica in open(ime_dat):
        vrstica = vrstica.split(",")
        if oseba1 in vrstica:
            seznam1.append(vrstica[0])

        if oseba2 in vrstica:
            seznam2.append(vrstica[0])
  
    for e1 in seznam1:
        if e1 in seznam2:
            sez.append(e1)

        if e1 not in sez_vse:
            sez_vse.append(e1)
    
    for e2 in seznam2:
        if e2 not in sez_vse:
            sez_vse.append(e2)
    
    povprecje = len(sez) / len(sez_vse)
    return(povprecje)
vrne = podobnost_oseb("drazba.txt", "Cilka", "Ema")
print(vrne)

