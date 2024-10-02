def najmanjsi_poz(s):
    min = 10000000
    neg_st = 0

    for e in s:
        if e > 0:
            if e < min:
                min = e

        
        else:
            neg_st += 1


    if neg_st == len(s):
        return None
            
    return min

vrne = najmanjsi_poz([-2, -3, -5])
print(vrne)
    

