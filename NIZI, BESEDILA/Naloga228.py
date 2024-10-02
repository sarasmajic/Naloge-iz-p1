prepovedane = {"zadnjica", "tepec", "pujs", "kreten"}

def cenzura(besedilo, prepovedane):
    string = ""

    beseda_besedilo = besedilo.split(" ") #seznam besed

    for beseda in beseda_besedilo:
        beseda = beseda.lower()
        if beseda in prepovedane:
            nova_beseda = beseda.replace(beseda, len(beseda) * "X")
            string += nova_beseda + " "
        else:
            string += beseda + " "
    print(string)
            #print(nova_beseda) -- prov pride

            
    
        

vrne = cenzura("Pepe je ena navadna ZadnJica in pUjs in še kaj hujšega", prepovedane)
print(vrne)