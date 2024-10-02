def dan_v_letu(dan, mesec):
    vsota = 0
    
    seznam = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(mesec - 1):
        vsota += seznam[i]
    
        if mesec == 1:
            vsota = 0
        
    iskan_dan = vsota + dan
    

    return iskan_dan


    
    



vrne = dan_v_letu(26, 2)
print(vrne)