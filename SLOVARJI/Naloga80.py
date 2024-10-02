def najraznolika(s):
    #slovar_crk = {}

    for beseda in s:
        #print(beseda)  -- vrne besede!
        beseda = beseda.lower()  #da vse crke v lower case
        #print(beseda)

        slovar_crk = {} #ce bi bil zunaj, bi pisalo za vse crke kolikokrat se pojavijo, tako pa kaze za vsako besedo
    
        for crka in beseda:
            #print(crka) -- vrne crke

            if crka not in slovar_crk:
                slovar_crk[crka] = 1
            else:
                slovar_crk[crka] += 1
            
        vrednost =0
        max = -100
        for kljuc in slovar_crk.items():
            vrednost += 1
            if max < vrednost:
                max = vrednost
                najraznolika_beseda = beseda



    print(max)   ###treba izpisat se to besedo!!!!!!!!
            
    
        
        
    
    


    



vrne = najraznolika(["RABarbara", "izpit", "zmagA"])
print(vrne)