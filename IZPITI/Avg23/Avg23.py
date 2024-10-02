#1
def nestrinjanja(ovire1, ovire2):
    seznam = set()
    for ovira1 in ovire1:
        for ovira2 in ovire2:
            if ovira1 not in ovire2:
                seznam.add(ovira1)
            
            if ovira2 not in ovire1:
                seznam.add(ovira2)
    
    return seznam
            #print(ovira2)


vrne = nestrinjanja(["sara", "gregor", "pameten"], ["ata", "mama", "gregor", "sonja"])
print(vrne)

#2
def dolzina_ovir(ime_datoteke):
    vsota = 0
    for vrstica in open(ime_datoteke):
        vrstica = vrstica.split("-")
        vr = vrstica[1]
        vr = vr.split(" ")  #vr je druga cifra
        #print(vrstica[0])
        
        prva_cifra = int(vrstica[0])
        druga_cifra = int(vr[0])
        
        razlika = (druga_cifra - prva_cifra) + 1
        #print(razlika) 3 3 2 2


        vsota = vsota + razlika
    return vsota 
       # prva_cifra = int(vrstica[0])
        #druga_cifra = int(vrstica[2])
        #razlika = druga_cifra - prva_cifra + 1
        #print(razlika)

vrne = dolzina_ovir("Avg23-ovire.txt")
print(vrne)