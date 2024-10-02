#vsak znak se lahko pojavi samo enkrat ali ničkrat -- če se samo 1x/0x potem vrne true

def samo_enkrat(s):
    znaki = {}  

    for znak in s:
        #print(znak) - abc
        if znak not in znaki:
            znaki[znak] = 1 #ce znaka ni v slovarju(kar ni) naj nastavi njegovo vrednost na 1(enkrat že viden)
        else:
            znaki[znak] += 1

    for crka, vrednost in znaki.items():
        if vrednost == 1 or vrednost == 0:
            pass
        else:
            return False
    
    return True
    

vrne = samo_enkrat("baa")
print(vrne)