import random

def nasledniki(s):
    besede = s.split(" ")
    slovar = {}


    for i in range(len(besede) - 1):
        #print(besede[i]) -- izpise besede
        if besede[i] not in slovar:
            slovar[besede[i]] = [] #ce besede ni v slovarju, naj se ustvari kljuc, katerega vrednost je prazen seznam.
            #in: [], to: [] itd...
        
        slovar[besede[i]].append(besede[i + 1])
            
    
    return slovar


vrne = nasledniki('in to in ono in to smo mi')
print(vrne)



def filozofiraj(besede, dolzine):
    for i in range(dolzine):
        #print(i) -- vrne 5
        prvabes, naslednik = random.choice(besede.items())
        print(prvabes)


vrn = filozofiraj({'in': ['to', 'ono', 'to'], 'to': ['in', 'smo'], 'ono': ['in'], 'smo': ['mi']}, 5)
print(vrne)