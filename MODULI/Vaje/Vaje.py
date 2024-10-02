import os

def kodirnik_postaja():
    slovar = {}
    string = ""

    files = os.listdir("vreme-po-sloveniji")
    for e in files:
        csv = open("vreme-po-sloveniji/" + e)
        for x in csv:
            x = x.split(",")

            if x[5] != '"NAME"':
                kraj = x[5][1:]
                kraj = kraj[0] + kraj[1:].lower()
                kraj = kraj.split(" ")
                for i in range(len(kraj)):
                    if i > 0:
                        kraj[i] = kraj[i][0].upper() + kraj[i][1:]
                sep = " "
                rez = sep.join(kraj)
                slovar[rez] = e.split(".")[0]

    return(slovar)

vrne = kodirnik_postaja()
print(vrne)

popravki = {'Murska Sobota Rakican': 'Murska Sobota',
            'Crnomelj Doblice':'Črnomelj',
            'Letalisce Edvarda Rusjana Mari': 'Maribor',
            'Letalisce Jozeta Pucnika Ljubl': 'Ljubljana',
            'Kocevje': 'Kočevje',
            'Smartno Pri Slovenj Gradcu': 'Smartno pri Slovenj Gradcu',
            'Kredarica': 'Kredarica',
            'Veliki Dolenci': 'Veliki Dolenci',
            'Novo Mesto': 'Novo mesto',
            'Nova Vas Na Blokah': 'Bloke',
            'Celje Medlog': 'Celje',
            'Portoroz Letalisce': 'Portorož',
            'Topol Pri Medvodah': 'Topol pri Medvodah',
            'Ratece Planica': 'Rateče'
           }

print("----")
def popravi(kodirnik):
    slovar = kodirnik_postaja()
    for kljuc in popravki:
        if kljuc in slovar:
            vrednost = slovar[kljuc]
            del slovar[kljuc]
            slovar[popravki[kljuc]] = vrednost
      
    return(slovar)
vrne = popravi(popravki)
print(vrne)

print()

def preberi_meritve(ime_postaje, kodirnik):
    string = ""
    slovar = {}

    koda = kodirnik[ime_postaje]
    print(koda)
    return 0
     #files = os.listdir("vreme-po-sloveniji") -- pogleda kiri so usi file v vreme-po-slo
    #for e in files: #izpise kaj je v tej mapi, keri filei
    csv = open("vreme-po-sloveniji/" + koda + ".csv")
    for x in csv:
        x = x.split(",")
    

        t = (x[11])
        for znak in t:
            if znak.isnumeric() == True:
                string += znak
            else:
                if len(string) == 0:
                    continue
                else:
                    string = int(string)
                    string = (string / 10)
                    print(string)
                    string = ""


   
  
    #if (leto,mes,dan) not in slovar:

              



vrne = preberi_meritve("Kredarica", vrne) #v sp. vrne je to kar vrne funkcija popravi(slovar)
print(vrne)