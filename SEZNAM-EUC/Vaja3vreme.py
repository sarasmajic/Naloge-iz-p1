#1
def najisje_temp(ime_dat, kraj):
    seznam = []

    for vrstica in open(ime_dat):
        vrstica = vrstica.strip()
        vrstica = vrstica.split(",") #vrstica je seznam z podatki
        datum = vrstica[1].split("-")

        
        if kraj == vrstica[0] and datum[0] == 2022:
            seznam.append(vrstica[2])

        return seznam
    #return seznam

vrne = najisje_temp("vreme.txt", "Ljubljana")
print(vrne)

#2
def povprecne_temp(ime_dat, kraj):
    seznam_temp_leto = []
    vsota =0

    for vrstica in open(ime_dat):
        vrstica = vrstica.strip()
        vrstica = vrstica.split(",") #vrstica je seznam z podatki
        datum = vrstica[1].split("-")

        if kraj == vrstica[0]:
            seznam_temp_leto.append(int(vrstica[2]))
    
    for temp in seznam_temp_leto:
        vsota += temp
    
    povprecje = vsota / len(seznam_temp_leto)
    return(povprecje)

vrne = povprecne_temp("vreme.txt", "Ljubljana")
print(vrne)

#nalog nisem nadaljevala, ker sem imela probleme z datoteko vremenske-postaje.txt