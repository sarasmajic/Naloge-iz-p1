def tocen(red, dejansko):
    razlika = 0
    for i in range(len(red)):
        for j in range(len(dejansko)):
            if i == j:
                razlika = dejansko[i] - red[i]

        #print(razlika)
        if razlika < 21:
            continue
        else:
            return False

    return True  
        
                #print(razlika) -- 0, 10, 20
    
vrne = tocen([800, 1200, 1500], [820, 1200, 1510])
print(vrne)


def tocni(redi, dejanski):
    pass
    #for i in range(len(redi)):
        #print(redi[i]) -- vsi 4 seznami
        #print(redi[0]) -- printa prvi seznam (570, 590, 616, 620)
        #for j in range(len(dejanski)):
         #   if i == j:

          #      if tocen(i,j) == True:
           #         print(i)

                  #  print(i)
                
        


vrne = tocni([[570, 590, 616, 620], [1200, 1500], [800, 900, 1000], [700, 800]], [[570, 611, 622, 630], [1200, 1510], [810, 910, 1000], [800, 900]])
print(vrne)


print()

#2
def enaki(linija1, linija2):

    for e in linija1:
        e = e.split(" - ")
   
    for e2 in linija2:
        e2 = e2.split(" - ")
        #print(e2)

        for i in range(len(e)):
            for j in range(len(e2)):
                if e[0] == e2[0] and e[-1] == e2[-1] and e2[i] in e or e[i] in e2:
                    continue
        
                else:
                    return False

    return True
                    
        

vrne = enaki(["Ljubljana - Kresnice - Zidani Most"], ["Ljubljana - Zagorje - Zidani most"])
print(vrne)