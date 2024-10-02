from bs4 import BeautifulSoup

def funkcija(ime_fila):

    data = open(ime_fila).read()
    #print(data)

    soup = BeautifulSoup(data)

    tag = soup.find_all("tr")

    slovar = {}

    for e in tag:
        if len(e.find_all("td")) > 0:

            oktanski = e.find_all("td")[1].string
            if "EUR" in oktanski:
                slovar["drzava"] = oktanski
                drzava = e.find_all("td")[0]
                print(drzava)
                #print(slovar)
                #print(oktanski)
                
        
rezultat = funkcija("Cene goriv po Evropi AMZS.html")    
   
   
   
   
    #if len(e.find_all("td")) > 0:
    #    temp = e.find_all("td")[3].string
    #    cela_vrstica = e.find_all("td")[0].string
