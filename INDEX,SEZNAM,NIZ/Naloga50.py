def je_zenska(emso): #vrne true ce zenska, false ce moski

    for i in range(len(emso)):
        c = int(emso[9:12]) #ta tri stevila so nizi, treba jih je convertat v inte

        #skupaj = c + 1 -- za delovanje ce iz str v int
    #print(skupaj)
    #print(c)

        if 000 < c <= 499:
            return False
        
        if 500 <= c <= 999:
            return True



vrne = je_zenska("2005004505002") #notr kot arg dobi niz(emso cifro)
print(vrne)