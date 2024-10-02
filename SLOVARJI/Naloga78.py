def pokazi_crke(beseda, crke):

    nova_beseda = ""
    
    for i in range(len(beseda)):
        #beseda[i] -- CRKE
        #i[0] -- NC NI!

        if beseda[i] in crke:
            nova_beseda = nova_beseda + beseda[i]
        else:
            nova_beseda = nova_beseda + "."

    return nova_beseda


vrne = pokazi_crke("PONUDNIK", set(["P", "O", "K", "N", "I", "U"]))
print(vrne)