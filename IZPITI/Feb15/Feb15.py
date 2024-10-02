#3
def dopis(kdo, komu, relacije):
        if kdo not in relacije:
            k = set()
            relacije[kdo] = k
            k.add(komu)
        else:
            relacije[kdo].add(komu)
    
        return(relacije)

vrne = dopis("Ana", "Berta", {})
print(vrne)

def najzgovornejsi(relacije):
    max = -100
    for kljuc in relacije:
        #print(relacije[kljuc]) vrne sete vrednosti
        if len(relacije[kljuc]) > max:
            max = len(relacije[kljuc])
            oseba = kljuc
    return oseba
    
vrne = najzgovornejsi({"Ana": {"Berta", "Cilka", "Dani"}, "Berta": {"Cilka"}})
print(vrne)

print("------------------")

def vse_osebe(relacije):
    mnozica_oseb = set()
    for kljuc in relacije:
        if kljuc not in mnozica_oseb:
                mnozica_oseb.add(kljuc)

        for vrednosti in relacije[kljuc]:
            if vrednosti not in mnozica_oseb:
                mnozica_oseb.add(vrednosti)
            
    
    return(mnozica_oseb)
        
vrne = vse_osebe({"Ana": {"Berta", "Cilka", "Dani"}, "Berta": {"Cilka"}})
print(vrne)

print(".............")

def neznanci(ime, relacije):
    mnozica = set()
    for kljuc in relacije:
    
        for vrednosti in relacije[kljuc]: #cilka berta dani cilka
          
             #print(relacije[ime]) #berta,dani,cilka
                if vrednosti not in relacije[ime]:
                    mnozica.add(vrednosti)
                if kljuc not in relacije[ime] and kljuc != ime:
                    mnozica.add(kljuc)
                else:
                    pass
        
      

    return mnozica 

   

vrne = neznanci("Berta", {"Ana": {"Berta", "Cilka", "Dani"},
                    "Berta": {"Cilka"},
                    "Cilka": set(),
                    "Ema": {"Cilka", "Fanci", "Greta"}})
print(vrne)

print("////////////")

#1 najprej lihi (naredi nov seznam)
def najprej_lihi(s):
    seznam = []

    for cifra in s:
        if cifra % 2 != 0:
            seznam.append(cifra)
            
    
    for c in s:
        if c % 2 == 0:
            seznam.append(c)
    
    print(seznam)
            
vrne = najprej_lihi([5, 8, 4, 17, 10, 9, 13])
print(vrne)