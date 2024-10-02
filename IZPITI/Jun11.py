# 1) Napiši funkcijo lihoNe7(sez), 
# ki kot argument prejme seznam in vrne največji element, 
# ki je lih in ni deljiv s 7. Predpostaviti smeš, da seznam ni prazen 
# in vsebuje le cela števila, med katerimi je vsaj eno liho in nedeljivo s 7.

def lihoNe7(sez):
    max = -1000
    for e in sez:
        if max < e and e % 2 != 0 and e % 7 != 0:
            max = e
    
    return max


vrne = lihoNe7([3, 14, 21, 5, 8, 22])
print(vrne)


print ()

#2
def sodiLihi(sez):
    for i in range(len(sez)):
        if (i % 2 != 0 and sez[i] % 2 == 0) or (i % 2 == 0 and sez[i] % 2 == 0) or len(sez) == 1:
            return True
        else:
            return False
                
                
            

vrne = sodiLihi([3])
print(vrne)

print()

#3 anagrami
def anagram(beseda1, beseda2):
    slovar1 = {}
    slovar2 = {}
    for crka in beseda1:
        if crka not in slovar1:
            slovar1[crka] = 1
        else: 
            slovar1[crka] += 1
    

    for crka2 in beseda2:
        if crka2 not in slovar2:
            slovar2[crka2] = 1
        else:
            slovar2[crka2] += 1
    
    if slovar1 == slovar2:
        return True
    else:
        return False



vrne = anagram("tipka", "piikat")
print(vrne)

#4 indeksiranje nizov

