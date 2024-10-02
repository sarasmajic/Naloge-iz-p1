def eboran(stavek):
    string = ""

    besede = stavek.split(" ")
    for beseda in besede:
           # if "." in beseda or ":" in beseda or "," in beseda or '"' in beseda or " " in beseda:
            #   ta_beseda = beseda
              # print(ta_beseda)
            #else:
                string += beseda[::-1] + " "

    print(string)

vrne = eboran('zapel je: "vse je narobe, tudi tale stavek."')
print(vrne)

def eboran2(stavek2):  ##nedokoncano
    string2 = ""

    besede = stavek2.split(" ")
    for beseda in besede:
        for i in range(len(beseda)):
            crka = beseda[i]
            if "." == crka or ":" == beseda[i] or "," == beseda[i] or '"' == beseda[i] or " " == beseda[i]:
                indeks = i
                znak = crka
                

        
         #   locilo = 
          #  beseda1 = beseda
           # print(locilo, beseda1)
        


vrne = eboran2('zapel je: "vse je narobe, tudi tale stavek."')
print(vrne)