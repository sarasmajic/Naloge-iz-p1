def najdaljsa_beseda(s):
    max = -100000
    besede = s.split(" ")
    #najd_bes = None --> za inicializacijo, ampak ne rabim
    for posamicna_beseda in besede:
        dolzina = len(posamicna_beseda)
        if dolzina > max:
            max = dolzina
            najd_bes = posamicna_beseda
        
    #print(najd_bes) #kako naj printam to besedo  (zgorna vrstica odg)
    
    return najd_bes
    
    


vrne = najdaljsa_beseda("An ban pet podgan")
print(vrne)








