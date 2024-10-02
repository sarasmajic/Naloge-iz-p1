#1
def v_karanteno(aktivnosti, okuzene):
    

    for ime in okuzene: 
        for oseba in aktivnosti: #oseba je kljuc npr ana, berta
            for akt in aktivnosti[ime]:
                if akt in aktivnosti[oseba] and oseba != ime:
                    isk_os = oseba
                    return isk_os
            
                    
  
    #print(kar)

            #if aktivnosti[ime] == aktivnosti[oseba] and oseba != ime:
             #   iskana_oseba = oseba
    #print(iskana_oseba)
            #print(aktivnosti[oseba])
    
            #print(aktivnosti[ime]) #[kava, telovad] [telovadba, frizer]

vrne = v_karanteno({
            "Ana": ["kava", "trgovina", "kava", "burek"],
            "Berta": ["telovadba", "frizer"],
            "Cilka": ["telovadba"],
            "Dani": [],
            "Ema": ["kava", "telovadba"],
            "Fanči": ["frizer"],
            "Greta": ["lokostrelstvo", "kolesarjenje"]
        } , ["Berta"])
print(vrne)

#2 genom sars covid
def trojke(s, n):
    pass
    #for i in range(len(s)):
     #   trojka = (s[:3])
      #  print(trojka)
        

#vrne = trojke("acgtacgatacgacg", 5)
#print(vrne)

#3 statistika
def statistika(podatki, drzava, n):
    p = podatki.split(":") #p je seznam

    print(p)

vrne = statistika("""Slovenija:31,20,25,14,50,60
Hrvaška:150,170,200,220,221
Madžarska:100,70,35""", "Slovenija", 3)
print(vrne)

#4 okuzeni
