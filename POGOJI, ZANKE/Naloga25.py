def vsaj_eno_liho(s):
    liha_st = 0

    for e in s:
        #if e % 2 == 0:
            #soda_st += 1
        
        if e % 2 != 0:
            liha_st += 1
        
    if liha_st > 0:  #ta del je zunaj for loopa, problem je ker recimo
        #pri 0 je liha_st = 0 in returna False in se funkcija konča
        return True
    if liha_st == 0:
        return False
                
    
    #print(liha_st) --> za delovanje

        #if liha_st > 0:
         #   return True
        #if liha_st == 0:
         #   return False
        
    
vrne = vsaj_eno_liho([0, 1, 3, 2, 6])
print(vrne)
