def anagram(b1, b2):
    crke_slovar1 = {}
    crke_slovar2 = {}

    for crka in b1:
        #print(crka) #p i r a t

        if crka not in crke_slovar1:
            crke_slovar1[crka] = 1
        else:
            crke_slovar1[crka] += 1
    

    for crka in b2:
        if crka not in crke_slovar2:
            crke_slovar2[crka] = 1
        else:
            crke_slovar2[crka] += 1
        
    #print(crke_slovar1, crke_slovar2)

    if crke_slovar1 == crke_slovar2:
        return True
    else:
        return False

    


vrne = anagram("sara", "rasa")
print(vrne)