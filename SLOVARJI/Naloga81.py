def najpogostejsa_beseda(s):
    besede = s.split(" ")
    #besede je seznam

    slovar = {}

    for beseda in besede:
        if beseda not in slovar:
            slovar[beseda] = 1
        else:
            slovar[beseda] += 1
        
    max = 0
    for kljuc, vrednost in slovar.items():
        if max < vrednost:
            max = vrednost
            iskana_beseda = kljuc
        
    #return iskana_beseda

    

vrne = najpogostejsa_beseda('in to in ono in to smo mi')
print(vrne)




def najpogostejsi_znak(s):
    slovar_znaki = {}

    for crka in s:
        if crka not in slovar_znaki:
            slovar_znaki[crka] = 1
        else:
            slovar_znaki[crka] += 1
        
    #print(slovar_znaki)
    maxx = 0
    for kljuc, vrednost in slovar_znaki.items():
        if maxx < vrednost:
            maxx = vrednost
            iskan_znak = kljuc
    return iskan_znak

 

vrn = najpogostejsi_znak("inxxtoxxinxxonoxxinxxtoxxsmoxxmi")
print(vrn)