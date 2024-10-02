def preveri_emso(emso):
    for i in range(13): #emso je dolg 13 st
        #print(i)
        
        c = int(emso[i])

        if i == 0:
            c1 = c * 7
        
        if i == 7:
            c2 = c * 7
        
        if i == 1:
            c3 = c * 6

        if i == 8:
            c4 = c * 6
        
        if i == 2:
            c5 = c * 5
        
        if i == 9:
            c6 = c * 5

        if i == 3:
            c7 = c * 4
        
        if i == 10:
            c8 = c * 4

        if i == 4:
            c9 = c * 3
        
        if i == 11:
            c10 = c * 3

        if i == 5:
            c11 = c * 2
        
        if i == 12:
            c12 = c * 2

        if i == 6:
            c13 = c * 2


    if int(emso[-1]) + (c1 + c3 +c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13) % 11 == 0:
        return True 
        
    else:
        return False


    #print(emso[-1]) -- za zadnjo cifro v emsu

        
        
        #print(c)
    

        


vrne = preveri_emso("20050045050040") #120
print(vrne)