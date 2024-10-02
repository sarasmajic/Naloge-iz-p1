def trojke(s):
    stevilo = 0
    for seznam in s:
        #print(seznam)
        if (seznam[0] + seznam[1]) == seznam[2]:
            stevilo += 1
        
    if stevilo == len(s):
        return True
    else:
        return False

    #print(stevilo)

    
vrne = trojke([(3, 5, 8), (2, 6 , 9), (1, 1, 2), (10, 5, 15)])
print(vrne)
