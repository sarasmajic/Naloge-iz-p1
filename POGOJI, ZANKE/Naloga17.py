#PRVI DEL


#def stevilo_ajev(beseda):  
    #stevilo_a = 0
    #for crka in beseda:
        #if crka == "a":
            #stevilo_a += 1  #naj vsakič ko vidi a, prišteje 1
    
    #return stevilo_a

#beseda = input("Vnesi stavek: ")  #input se ponavadi zmeraj piše zunaj definicije
#vrne = stevilo_ajev(beseda) #ta beseda je od inputa in to prejme kot argument, ko kliče funkcijo (kir primer naj uporabi za delovanje funckije)
#print(vrne)

#TRETJI DEL



#DRUGI DEL
def stevilo_znakov(beseda, znak):
    stevilo_z = 0
    for z in beseda:
        if znak == z:
            stevilo_z += 1
    

    return stevilo_z


beseda = input("dej besedo: ")
zn = input("Kateri znak želiš: ")
vraca = stevilo_znakov(beseda, zn)
#print(vraca)


def stevilo_ajev(beseda):
    st_z = stevilo_znakov(beseda, "a")
    return st_z


v = stevilo_ajev(beseda)
print(v)

