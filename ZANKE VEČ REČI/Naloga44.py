def se_ujema(beseda, vzorec): #ML..O

    if len(beseda) != len(vzorec):
        return False

    #for i in range(5): #ustvari seznam s stevilkami 01234, s temu lahko dodas to besedi da posices index, ce nveš njene dolzine
    for i in range(len(vzorec)):
        if beseda[i] == vzorec[i] or vzorec[i] == ".":
            pass #ignorira ta instruction, itak gre naprej u for loop in izvaja iteracijo
    
        else:
            return False

    return True










def prva_beseda(besede, vzorec):  #besede je seznam z besedami
    #vzorec = "DR..."


    for beseda in besede:
        if se_ujema(beseda, vzorec):
            return beseda

    return None    
    




vrne = prva_beseda(["DORA", "MORALNA", "DREVJE", "DREVO"], "DR...")
print(vrne)