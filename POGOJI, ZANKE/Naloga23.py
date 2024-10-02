def poprecje_brez(s):
    povprecna_teza = 0
    rezultat = 0
    max = -10000
    min = 1000000
    for teza in s:
        if teza > max:
            max = teza

        if teza < min:
            min = teza
    #print(max)
    #print(min)  ---> da se preveri delovanje, PAZI DA JE PO IF STAVKU IN KJE JE POSTAVLJEN KER 
    #KODA NAPREJ JE ZNOTRAJ FOR LOOPA IN JE COMPILER CONFUSED
        
        povprecna_teza += teza
    #print(povprecna_teza) --> za delovanje
    #print(povprecna_teza - max - min) --> za delovanje
    #print(len(s)) --> za delovanje
    
    rezultat = (povprecna_teza - max - min) / (len(s) - 2)
    print(rezultat)

    #return rezultat

vrne = poprecje_brez([1, 10, 5, 5, 5, 1])
print(vrne)