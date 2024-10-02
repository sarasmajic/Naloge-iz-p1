def se_ujema(beseda, vzorec): #ML..O
    

#for i in range(5): #ustvari seznam s stevilkami 01234, s temu lahko dodas to besedi da posices index, ce nveš njene dolzine
    for i in range(len(beseda)):
        if beseda[i] == vzorec[i] or vzorec[i] == ".":
            pass #ignorira ta instruction, itak gre naprej u for loop in izvaja iteracijo
    
        else:
            return False

    return True


vrne = se_ujema("MLEKO", "ML..O")
print(vrne)
 