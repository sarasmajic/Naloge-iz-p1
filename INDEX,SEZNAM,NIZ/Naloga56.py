def mesta_crke(beseda, crka):
    for i in range(len(beseda)):
        #print(i) 01234567
        #print(beseda[i]) ponudnik
        #print(crka) NNNNNN

       if beseda[i] == crka:
           print(i)




vrne = mesta_crke("RABARBARA", "R")
print(vrne)