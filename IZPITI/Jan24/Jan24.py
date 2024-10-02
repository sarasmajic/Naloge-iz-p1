import numpy as np
from bs4 import BeautifulSoup


def knjigovodstvo(ime_datoteke):
    prihodki = []
    odhodki = []
    vsota = 0


    for vrstica in open(ime_datoteke):
        vrstica = vrstica.split(":") #vrstica je seznam
        cifra = int(vrstica[1])
        
        if cifra > 0:
            iskan_stvar = vrstica[0]
            prihodki.append((iskan_stvar , cifra))
        
        if cifra < 0:
            isk_stvar = vrstica[0]
            odhodki.append((isk_stvar, cifra))

        vsota = vsota + cifra

    print(prihodki)
    print(odhodki)
    print(vsota)
        
vrne = knjigovodstvo("Jan1-24-kvodstvo.txt")
print(vrne)

print("...................")

#2 draginja
def draginja(odhodki):
    slovar_cen = {}
    slovar_stevcev = {}
    stevec = 0
    seznam = []

    for e in odhodki:
        predmet = e[0]
        cena = e[1]

        if predmet not in slovar_cen:
            slovar_cen[predmet] = cena
        else:
            slovar_cen[predmet] += cena
        
        if predmet not in slovar_stevcev:
            slovar_stevcev[predmet] = 1
        else:
            slovar_stevcev[predmet] += 1

    povprecje = 0
    for predmet in slovar_cen:
        if predmet in slovar_stevcev:
            povprecje = slovar_cen[predmet] / slovar_stevcev[predmet]
        
        seznam.append((predmet, povprecje))

#for kljuc, vrednost in slovar_cen.items():
 #       for key, value in slovar_stevcev.items():
  #          povprecje = vrednost / value    #NE DELA KER ITERIRA VSAK Z VSAKMUKAR NI LOGICNO
   #     print(povprecje)
    
        #seznam.append((povprecje, kljuc))
    #print(seznam)
    
    max = -1000
    for terka in seznam:
        stvar = terka[0]
        povp = int(terka[1])
        if max < povp:
           max = povp
           max_povp = stvar
    
    return max_povp

vrne = draginja([("stol", 20), ("torba", 12), ("tempera", 3), ("miza", 50), ("stol", 30), ("stol", 60), ("miza", 40), ("torba", 5)])
print(vrne)

print("................")


def evidenca(postavke, ime_datoteke):
    #print(postavke[0]) vrne prov prvo terko

    f = open(ime_datoteke, "w")

    f.write(f"{'Stvar':6}{'Cena X Kosov':>20}{'Skupaj':>20}\n")
    f.write("-" * (6 + 40) + "\n")

    for p in postavke:
        vsota = 0
        predmet = p[0]
        cena = p[1]
        kos = p[2]
        vsota = cena * kos
        f.write(f"{predmet:<8}{cena:>10}{'x':>2}{kos:>3}{vsota:>23}\n")

    

vrne = evidenca([("slika", 50, 2),("tempera", 3, 1),("stol", 20, 1),("kip", 20, 12),("zrak", 0, 141),("torba", 12, 1)], "Jan1-24-zapis.txt")
print(vrne)


#3 dragocenosti

stvari = np.array(["skatla", "nakit", "skatla", "skatla"])
cene = np.array([[13.2, 1], [11.8, 2], [2.1, 3], [7.1, 4]])
meja = 5.1

# x[vrstica, stolpec]
# x[:, 0] -> prvi stolpec
# x[0, :] -> prva vrstica

prvi_stolpec_cene = cene[:,0]
vecje = (prvi_stolpec_cene > meja)
print(set(stvari[vecje]))

print(prvi_stolpec_cene)

#print(stvari)
#print(cene)
#print(meja) """

def spletno_knjigovodstvo(ime_datoteke):
    string = ""
    seznam1 = []
    seznam2 = []
    seznam = []
    data = open(ime_datoteke).read()

    soup = BeautifulSoup(data)

    tag = soup.find_all("dt")

    for e in tag:
        predmet = e.string
        seznam1.append(predmet)

    
    tag2 = soup.find_all("dd")
    for e2 in tag2:
        stavek = e2.string
        for crka in stavek:
            if crka.isnumeric() == True:
                string += crka
            else:
                if string != "":
                    seznam2.append((int(string)))
              
                string = ""
   
    for i in range(len(seznam1)):
        seznam.append((seznam1[i], seznam2[i]))

    return seznam
       # print(stavek)
   # print(tag2)
    
vrne = spletno_knjigovodstvo("knjigovodstvo.html")
print(vrne)




