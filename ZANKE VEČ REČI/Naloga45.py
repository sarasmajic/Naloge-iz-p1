def skoki_zmagovalec(s1, s2):
    prva_drzava = 0
    druga_drzava = 0
    for i in range(len(s1)): #to je če sta seznama oba enako dolga
        #FOR I IN RANGE KER Z NAVADNIM FOR LOOPOM NEMORM CEZ DVA SEZNAMA

        if s1[i] == s2[i]:
            prva_drzava += 0.5    #če tale drzi gre naprej in if stavek nebi drzal zato bo slo naprej na else ker je else v if stavku
            druga_drzava += 0.5

        elif s1[i] > s2[i]:
            prva_drzava += 1  #vsi trije stavki so povezani
        
        else:
            druga_drzava += 1
        
    
    if prva_drzava == druga_drzava:
        return None
    
    elif prva_drzava > druga_drzava:
        return 1
    
    else:
        return 2



vrne = skoki_zmagovalec([153, 141, 152, 148, 135], [148, 148, 148, 148, 148])
print(vrne)