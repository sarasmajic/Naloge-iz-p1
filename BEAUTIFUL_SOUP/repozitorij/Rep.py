from bs4 import BeautifulSoup

def funkcija(ime_fila):

    data = open(ime_fila).read()
    #print(data)

    soup = BeautifulSoup(data)

    tag = soup.find_all("h3")

    slovar = {}
    slovar2 = {}
    slovar3 = {}
   

    for e in tag:
        if len(e.find_all("a")) > 0:
            ime_rep = e.find_all("a")

            for x in ime_rep:
                naslov = x.string
                naslov = naslov.strip()
                slovar["ime"]=naslov

        print(slovar)
             #   neki = (x.attrs["href"])
             #   print(neki)

    tag2 = soup.find_all("p")


    for y in tag2:
        #print(y)
        #print(y.attrs)
        if "itemprop" in y.attrs: #y.attrs je slovar, kljuc (itemprop, class). Preverimo če je itemprops kot ključ v slovarju
            #print(y)
            opis = y.string 
            opis = opis.strip()
            #print(opis)
        #print(opis)
            slovar2["opis"] = opis

        #print(opis)

            print(slovar2)

    tag3 = soup.find_all("span")

    for pl in tag3:
        if "itemprop" in pl.attrs:
            jezik = pl.string
            slovar3["jezik"] = jezik
            print(slovar3)
    #print(tag3)

vrne = funkcija("Repositories.html")



#tag = soup.find_all("tr")

   # slovar = {}

    #for e in tag:
        #if len(e.find_all("td")) > 0:
