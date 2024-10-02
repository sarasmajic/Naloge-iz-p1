def mrange(zac, fak, dol):
    seznam = []
    for i in range(dol):
        seznam.append(0) #nemore bit prazen seznam, ga zafilam z 0
        seznam[0] = zac #namest ničle damo 7 za prvo cifro, kot naloga zahteva



        if seznam[i] == 0:
            seznam[i] = seznam[i - 1] * fak
 

        #if seznam[i] > seznam[i + 1]: #7 vecji kot 0
        #   seznam[i + 1] = seznam[i] * fak                 --- KOMPLICIRANJE!!!
        
        
        #seznam[1] = (zac * fak) -- ne gre na tak nacin
        #seznam[]
    
        #print(seznam[i]) -- printa 700000
        #print(i)
    
    return seznam




vrne = mrange(7, 4, 5)
print(vrne)