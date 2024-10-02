import math



def sekata(krog1, krog2):
    
        x1 = krog1[0]
        y1 = krog1[1]
        r1 = krog1[2]
        #print(krog1[i]) -- vrne cifre
       
        x2 = krog2[0]
        y2 = krog2[1]
        r2 = krog2[2]
        vrednost_x = (x1 - x2) ** 2
            #print(vrednost_x)
        vrednost_y = (y1 - y2) ** 2
        skupna = math.sqrt(vrednost_x + vrednost_y)
            
        if skupna < (r1 + r2):
            return True
        else:
            return False
            #print(skupna)
            

vrne = sekata((1, 2, 1), (1, 3, 2))
print(vrne)

def sekajo(krogi):
    for i in krogi:
        for j in krogi:
            if i == j:
                continue

            if sekata(i, j) == True:
                return True
            
    return False

vrne = sekajo([(1, 2, 1), (1, 3, 2)])
print(vrne)