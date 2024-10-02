#Izpiši vse stvari, za katere se je zanimala Ana.
for vrstica in open("zapisnik.txt"):
    predmet, oseba, cena = vrstica.split(",")
    if oseba == "Ana":
        print(predmet)

print()

#slovar, katerega ključi so imena oseb, vrednosti pa seznam vseh predmetov, za katere se je zanimala ta oseba?
slovar = {}
for vrstica in open("zapisnik.txt"):
    predmet, oseba, cena = vrstica.split(",")

    if oseba not in slovar:
        slovar[oseba] = []
    
    if predmet not in slovar[oseba]: #ce predmeta ni v vrednosti kljuca ga potem dodaj
        slovar[oseba].append(predmet)

print(slovar)
print()

#Paranoični Cilki se zdi, da ima ena od ostalih nekaj proti njej.
# Izpiši ime osebe, ki je največkrat višala ponudbo (za določen predmet) neposredno za njo. 
# Pazi: tule Dani ni višala Cilkine ponudbe, ker gre za drug predmet.


#for i, (pr, os, ce) in enumerate ("zapisnik.txt"):
    #print(i)


#Izpiši vse ljudi, ki so se potegovali za kip in sicer v takšnem vrstnem redu, kot so se pojavljali.

print("------")
seznam_kip = []
for vrstica in open("zapisnik.txt"):
    predmet, oseba, cena = vrstica.split(",")
    if predmet == "kip":
        seznam_kip.append(oseba)
print(seznam_kip)

print("..........")


def izpadanje(ime_dat, pr):
    sez_vsega = []
    sez = []
  

    for vrstica in open(ime_dat):

        vrstica = vrstica.strip()
        vrstica = vrstica.split(",")

        if vrstica[0] == pr:
            sez_vsega.append(vrstica)

    sez_vsega = (sez_vsega[::-1])
    
    
    
    for e in sez_vsega:
        if e[1] not in sez:
            sez.append(e[1])
        else:
            continue
    
    print(sez[::-1])
        
vrne = izpadanje("zapisnik.txt", "Meldrumove vaze")
print(vrne)
