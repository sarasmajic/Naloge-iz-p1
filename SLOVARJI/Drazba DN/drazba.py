def najvisja_cena(dat):
    slovar = {}

    max = -1000
    for vrstica in open(dat):
        predmet, oseba, cena = vrstica.split(",")
        cena = int(cena)
        if cena > max:
            max = cena
            max_predmet = predmet
            max_oseba = oseba


    #print(cena, max_predmet, max_oseba)
        
vrne = najvisja_cena("drazba.txt")
print(vrne)


def koncne_cene(dat):
    slovar2 = {}

    for vrstica in open(dat):
        predmet, oseba, cena = vrstica.split(",")
        cena = int(cena)
        
        if predmet not in slovar2:
            slovar2[predmet] = []
        
        slovar2[predmet].append(cena)

    for s in slovar2:
        print(slovar2[s][-1])


vrn = koncne_cene("drazba.txt")
print(vrn)


#cene = {} #cene vseh predmetov           MOZNA RESITEV Z GETOM

#for vrstica in open("zapisnik.txt"):
#    predmet, oseba, cena_predmeta = vrstica.split(",") #trenutni predmet, oseba in cena

#    cena_predmeta = int(cena_predmeta)
#    if(cena_predmeta > cene.get(predmet, 0)): #če je trenutna cena predmeta > najvišja do sedaj videna cena predmeta
#        cene[predmet] = cena_predmeta (ta del)

#cene.get -- če v slovarju predmeta se ni, naj mu value nastavi na 0. Cena predmeta je recimo 5 
# kar je vecje kot 0 in se nastavi tako, ker se vedno gleda če je naslednja večja kot trenutna (ta del)

def ponudba(d):
    slovar3 = {}

    for vrstica in open(d):
        predmet, ime, cena = vrstica.split(",")
        #print(ime)

        if predmet not in slovar3:
            slovar3[predmet] = 1
        else:
            slovar3[predmet] += 1

    max = 0
    for key, value in slovar3.items():
        #print(key, value)
        if value > max:
            max = value
            isk_p = key
            print(isk_p)
    return slovar3
v = ponudba("drazba.txt")
print(v)


def porabla_oseba(d):
    slovar_oseb = {}
    for vrstica in open(d):
        predmet, oseba, cena = vrstica.split(",")
        cena = int(cena)

        if oseba not in slovar_oseb:
            slovar_oseb[oseba] = cena
        else:
            slovar_oseb[oseba] += cena
        
    print(slovar_oseb)

vrne = porabla_oseba("drazba.txt")
print(vrne)

def razlika(d):
    slovar_cen_razlika = {}

    for vrstica in open(d):
        predmet, oseba, cena = vrstica.split(",")
        cena = int(cena)

        if predmet not in slovar_cen_razlika:
            slovar_cen_razlika[predmet] = []
        
       
        slovar_cen_razlika[predmet].append(cena)
    
    for s in slovar_cen_razlika:
        razlika = 0
        zadnja_cifra = slovar_cen_razlika[s][-1]
        prva_cifra = slovar_cen_razlika[s][0]

        razlika = zadnja_cifra - prva_cifra
    
        
        print(razlika)

    #return slovar_cen_razlika
    


vrne = razlika("drazba.txt")
print(vrne)