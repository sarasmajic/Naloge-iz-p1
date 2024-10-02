#1
def skupne_povezave(pot1, pot2):
    stevec = 0

    if len(pot1) > len(pot2):
        dolzina = len(pot2)
    else:
        dolzina = len(pot1)
    
    for i in range(dolzina - 1):
        if pot1[i] == pot2[i] and pot1[i + 1] == pot2[i + 1]:
            stevec += 1
    
    return stevec
            
      

vrne = skupne_povezave("ABCDEFGH", "GHCDIFGHIJK")
print(vrne)

print("---------------------------")

#3
def preberi_zemljevid_povezav(ime_datoteke):
    slovar = {}

    for vrstica in open(ime_datoteke):
        vrstica = vrstica.split(":")
        par_faksa = vrstica[0]
        par_faksa = tuple(par_faksa.split("-")) #vrne seznam [BF, FRI] [BF, FDV]
    
    
        povezava_sez = vrstica[1].strip()
        povezava_sez = povezava_sez.split(",")
        
        for povezava in povezava_sez:
            if povezava == "":
                continue
            if povezava not in slovar:
                slovar[povezava] = par_faksa
            else:
                slovar[povezava] += par_faksa
        

    return slovar

vrne = preberi_zemljevid_povezav("zemljevid.txt")
print(vrne)

print("-----------------------------")

#2
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"
def najzahtevnejse(zemljevid):
    slovar = {} #crka bo kljuc, vrednost pa kolk povezav je


    for kljuc, value in zemljevid.items():
        
        for crka in kljuc: 
                    if crka not in slovar:
                        slovar[crka] = set(value.split(" "))
                    else:
                        slovar[crka].update(set(value.split(" "))) #problem je ker mi vse vrednosti od tm do tm
        
    print(slovar)
        
        


vrne = najzahtevnejse({
    (A, B): "gravel trava",
    (A, V): "pešci lonci",
    (B, C): "bolt lonci",
    (B, V): "",
    (C, R): "stopnice pešci lonci",
    (D, F): "stopnice pešci",
    (D, R): "pešci",
    (E, I): "trava lonci",
    (F, G): "trava črepinje",
    (G, H): "črepinje pešci",
    (G, I): "avtocesta",
    (H, J): "robnik bolt",
    (I, M): "avtocesta",
    (I, P): "gravel",
    (I, R): "stopnice robnik",
    (J, K): "",
    (J, L): "gravel bolt",
    (K, M): "stopnice bolt",
    (L, M): "robnik pešci",
    (M, N): "rodeo",
    (N, P): "gravel",
    (O, P): "gravel",
    (P, S): "",
    (R, U): "trava pešci",
    (R, V): "pešci lonci",
    (S, T): "robnik trava",
    (T, U): "gravel trava",
    (U, V): "robnik lonci trava"
}
)
print(vrne)