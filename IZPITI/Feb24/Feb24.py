#5 oblikovanje nizov
def vozni_redi(potniki, ime_datoteke):

    f = open(ime_datoteke, "w")

    for p in potniki:
        potnik = p[0]
        let = p[1]
        odhod = p[2]
        prihod = p[3]
        #print(prihod[0]) vrne prvo cifro tkoda je kul
    
        f.write(f"{potnik:<15}{let:>10}{odhod[0]:>15}{':'}{odhod[1]}{'-'}{prihod[0]}{':'}{prihod[1]}\n")


vrne = vozni_redi([("Ana Argon", "LH2832", (12, 10), (13, 20)), ("Berta Bor", "UO391", (15, 5), (20, 30)), ("Cilka Daner", "LH192", (7, 0), (12, 30))], "Feb24-5nal.txt")
print(vrne)


def preberi_sporocilo(ime_datoteke):

    ime = None
    sedez = None

    for vrstica in open(ime_datoteke):


        if ":" in vrstica:
            vrstica = vrstica.strip()
            vrstica = vrstica.split(":")
            iskana_vrstica = vrstica[1]

            iskana_vrstica = iskana_vrstica.strip()
        
            iskana_vrstica = iskana_vrstica.split(" ") #split ti vrne nazaj ze seznam

        #--------------------------------------------------------------------- 

            vrstica_ok = True

            if len(iskana_vrstica) >= 2: #and iskana_vrstica.isupper() == True:
                for beseda in iskana_vrstica:
                    if beseda[0].isupper() == True:
                        continue
                    else:
                        vrstica_ok = False  #okol obrnes problem, assumas da je vsaka vrstica okej, (tiste k so okej se shranijo v iskana_vrstica), gledas kira ni ok

            else:
                vrstica_ok = False

            #print(vrstica)
            #print(vrstica_ok)  

            iskana_vrstica_str = ' '.join(iskana_vrstica) #joina posamezne besede v seznamu v string
            if vrstica_ok == True:
                ime = iskana_vrstica_str
            else:
                continue  

    for vrstica in open(ime_datoteke):
        vrstica = vrstica.strip()
        vrstica = vrstica.split(" ")

        for beseda in vrstica:

            if len(beseda) >= 3:
                if beseda[0].isnumeric() and beseda[1].isnumeric() and beseda[2] in ["A", "B", "C", "D", "E", "F"]:
                    sedez = beseda

            if len(beseda) >= 2:
                if beseda[0].isnumeric() and beseda[1] in ["A", "B", "C", "D", "E", "F"]:
                    sedez = beseda


    sedez = sedez.replace(",", "")
    sedez = sedez.replace(".", "")
    sedez = sedez.replace("?","")

    return ime, sedez

        #print(vrstica)
    
            #print(iskana_vrstica)
            #beseda = iskana_vrstica.split(" ")
            #for beseda in iskana_vrstica:
             #   print(beseda)

vrne = preberi_sporocilo("sporocilo1.txt")
print(vrne)


print("----")

def razpored(seznam):
    slovar = {}

    for terka in seznam:
        ime = terka[0]
        zeljen_sedez = terka[1] #12A
        st_sedeza = int(zeljen_sedez[0:-1])
        crka_vrste = zeljen_sedez[-1]
        #print(crka_vrste)

        #print(st_sedeza) -- cifra sedeza

        while (str(st_sedeza) + crka_vrste ) in slovar:
            st_sedeza += 1

            if st_sedeza > 130:
                st_sedeza = 1
                if crka_vrste == "A":
                    crka_vrste ="B"
                if crka_vrste == "B":
                    crka_vrste = "C"
                if crka_vrste == "C":
                    crka_vrste = "D"
                if crka_vrste == "D":
                    crka_vrste = "E"
                if crka_vrste == "E":
                    crka_vrste = "F"


        slovar[str(st_sedeza) + crka_vrste] = ime 
            #slovar[str(st_sedeza) + crka_vrste] = ime
        
           #slovar[str(st_sedeza + 1) + crka_vrste] = ime
    seznam = []
    for kljuc, value in slovar.items():
        seznam.append((value, kljuc))
    
    return seznam
        #print(kljuc, value)
    #print(slovar)



        

vrne = razpored([("Ana", "12A"), ("Berta", "8D"), ("Ema", "5E"), ("Iva", "12C"),
                 ("Cilka", "8D"), ("Fanči", "12A"), ("Dani", "13A"), ("Greta", "12A"),
                 ("Helga", "4E"), ("Jana", "6E"), ("Klara", "5E"),
                 ("Liza", "123E"), ("Micka", "123F"), ("Nina", "123E")])
print(vrne)