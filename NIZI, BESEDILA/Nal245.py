
def navodila(zaporedje):
    seznam = []
    string = ""

    for i in range(len(zaporedje)):
        if zaporedje[i] == "L" or zaporedje[i] == "D":
            seznam.append(zaporedje[i])
        else:
            if zaporedje[i].isnumeric() == True:
    
                if zaporedje[i + 1].isnumeric():
                    #print(zaporedje[i+1])
                    string += zaporedje[i]
        
                    #string = int(string)
                   # seznam.append(string) ne appendava ker 3, 32, 322
                else:
                    string += zaporedje[i] #trenutni znak, ki je pred L/D
                    seznam.append(string)
                    string = ""
    return(seznam)
                


vrne = navodila("72D3L331L")
print(vrne)