def knjigovodtsvo(ime_datoteke):
    seznam_poz = []
    seznam_neg = []
    vsota = 0

    for vrstica in open(ime_datoteke):
        vrstica = vrstica.strip()
        vrstica = vrstica.split(":")
        vrstica[1] = int(vrstica[1])
   

        if vrstica[1] > 0:
            seznam_poz.append((vrstica[0], vrstica[1]))
        if vrstica[1] < 0:
            #vrstica[1] = abs(vrstica[1]) nesmes tuki ker potem se dol prenese in vsote ne izracuna prov
            seznam_neg.append((vrstica[0], abs(vrstica[1])))


        vsota += vrstica[1] 
    
    return(seznam_poz, seznam_neg, vsota)


vrne = knjigovodtsvo("knjigovodstvo.txt")
print(vrne)

print()

#2
def draginja(odhodki):
    slovar = {}
    max = -100

    for terka in odhodki:
        predmet = terka[0]
        cena = terka[1]
        if predmet not in slovar:
            slovar[predmet] = [cena]
        else:
            slovar[predmet].append(cena)
    
    for key, value in slovar.items():
        vsota = sum(value)
        povprecje = vsota / len(value)
        if povprecje > max:
            max = povprecje
            pred = key

    return pred
        #print(key, povprecje)
        #print(key, value)

vrne = draginja([('stol', 20), ('torba', 12), ('tempera', 3), ('miza', 50), ('stol', 30), ('stol', 60), ('miza', 40), ('torba', 5)])
print(vrne)

#4 spletno knjigovodstvo
from bs4 import BeautifulSoup

def funkcija(ime_fila):
    string = ""
    sez = []

    data = open(ime_fila).read()
    #print(data)

    soup = BeautifulSoup(data)

    tag = soup.find_all("dt")

    for e in tag:
        predmet = (e.string)
    
    tag2 = soup.find_all("dd")
    for e2 in tag2:
        stavek = (e2.string)
        for crka in stavek:
            if crka.isnumeric() == True:
                string += crka
               
            else:
                if len(string) == 0:
                    continue
                else:
                    sez.append((predmet, string))
                    #print(int(string))
                    string = ""
                #print(string)
        
  
    return(sez)
            
        
        
        #for crka in e2:

         #   print(crka)
   

vrne = funkcija("knjigovodstvo.html")
print(vrne)