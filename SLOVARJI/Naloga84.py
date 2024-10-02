def obv_sluzba(msg):
    besede = msg.split(" ")

    seznam_besed = {}

    for beseda in besede:
        if beseda[0].isupper():      #preveri kere besede se zacnejo z veliko crko
            #print(beseda)   -- vrne vse besede z veliko zacetnico

            if beseda not in seznam_besed:
                seznam_besed[beseda] = 1
            else:
                seznam_besed[beseda] += 1
    

    print(seznam_besed)
    
    #print(beseda) -- printa mi vse besede


vrne = obv_sluzba("""Dragi Ahmed kako si kaj Upam da so otroci že zdravi Mustafa Osama in jaz smo se šli danes malo razgledat in kaže kar dobro Abdulah pa ni mogel zraven je šel v Pešavar prodat še tri kamele Osama sicer pravi da se mu to pred zimo ne splača ampak saj veš kakšen je Abdulah tak je kot Harun nič jima ne dopoveš še Osama ne Jibril me kliče moram iti oglasi se kaj na Skype tvoj Husein""")
print(vrne)