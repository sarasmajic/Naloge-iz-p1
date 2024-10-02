def uravnotezena(tovor):
    ena_stran = []
    druga_stran = []

    for i in range(len(tovor)):
        if i % 2 == 0:
           ena_stran.append(tovor[i])
        else:
            if i % 2 != 0:
                druga_stran.append(tovor[i])
    
    vsota_ena = 0
    for e_ena in ena_stran:
        vsota_ena += e_ena

    vsota_druga = 0
    for e_druga in druga_stran:
        vsota_druga += e_druga
    
    if vsota_druga > vsota_ena:
        razlika = vsota_druga - vsota_ena
    else:
        razlika = vsota_ena - vsota_druga
    
    if razlika > 10:
        return False
    else:
        return True

    #print(razlika)
        
vrne = uravnotezena([2, 10, 3, 8, 1])
print(vrne)

print("------------")
#2
def deli(paketi, kapacitete):
    stanje = [0] * len(kapacitete) #naredi seznam [0,0,0]

   
    for teza in paketi:
        min = 100000
        ind_min = None
        for i, cifra in enumerate(stanje):
            if cifra < min and (teza + stanje[i] <= kapacitete[i]):
                ind_min = i
                min = cifra


        if ind_min == None:
            pass
        else:
            stanje[ind_min] += teza

    return stanje

vrne = deli([6, 4, 2, 1, 5, 1, 15], [5, 20, 7])
print(vrne)

print("------------")

def kontrola(ime): #ime je ime_datotekes
    seznam_preob = []

    for vrstica in open(ime):
        vrstica = vrstica.strip() #prvo strip potem split
        vrstica = vrstica.split(":")
        
        #print(vrstica) -- je seznam
        ladja = vrstica[0]
        nosilnost = int(vrstica[1])
        
        seznam_teze = vrstica[2].split(",")
        #print(seznam_teze)

        vsota = 0
        for teza in seznam_teze:
            teza = int(teza)
            vsota += teza
        print(vsota)


        if nosilnost < vsota:
            seznam_preob.append(ladja)
    
    return set(seznam_preob)

vrne = kontrola("nacrt9756.txt")
print(vrne)

print("--------------")

#nepravilno narejena naloga
def pravilna(marsovec, hierarhija, antene):
    for podrejeni in hierarhija[marsovec]:
        #print(podrejeni) -- printa podrejene od marsovca(torej elizabete npr)
        if antene[marsovec] < antene[podrejeni]:
            continue
        else:
            return False
    return True

#for kljuc in slovar1:
    #print(slovar1[kljuc])
    #print(slovar2[kljuc])   -- ce so isti kljuci


vrne = pravilna("Elizabeta", {"Adam": ["Matjaž", "Cilka", "Daniel"],
            "Aleksander": [],
            "Alenka": [],
            "Barbara": [],
            "Cilka": [],
            "Daniel": ["Elizabeta", "Hans"],
            "Erik": [],
            "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
            "Franc": [],
            "Herman": ["Margareta"],
            "Hans": ["Herman", "Erik"],
            "Jožef": ["Alenka", "Aleksander", "Petra"],
            "Jurij": ["Franc", "Jožef"],
            "Ludvik": [],
            "Margareta": [],
            "Matjaž": ["Viljem"],
            "Petra": [],
            "Tadeja": [],
            "Viljem": ["Tadeja"]}, {
            "Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83,
            "Viljem": 58, "Tadeja": 20, "Elizabeta": 68, "Hans": 64, "Ludvik": 50,
            "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32, "Franc": 30,
            "Jožef": 29, "Margareta": 3, "Alenka": 9, "Aleksander": 5, "Petra": 7} )
print(vrne)

