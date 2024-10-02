def slovar(dat):
    slovar = {}

    for vrstica in open(dat):
        stars, otrok = vrstica.split(" ")
        stars = stars.strip() #da se znebim backslasha
        otrok = otrok.strip()
        #print(stars, otrok)


        if stars not in slovar:
            slovar[stars] = []
        
        slovar[stars].append(otrok)
            

        
    print(slovar)



vrne = slovar("druzinsko-drevo.txt")
print(vrne)