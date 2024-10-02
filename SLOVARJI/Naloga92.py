import random

def grde_besede(stavek):
    grde_besede = {
    'kreten': ['kljukec'],
    'idiot': ['mentalno zaostala oseba', 'omejen clovek']
    }

    besede = stavek.split(" ")
    #print(beseda)

    
    for kljuc, vrednost in grde_besede.items():
        i = 0
        #print(kljuc, vrednost)
        for beseda in besede:
            i += 1
            if beseda == kljuc:
                vrednost = random.choice(vrednost)
                #print(vrednost) --> vrne random vrednost
                besede[i - 1] = vrednost
    

    string = " "
    return (string.join(besede))



    

vrne = grde_besede("Joj ta Python spet se počutim kot idiot")
print(vrne)