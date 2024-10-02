from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen("https://www.gutenberg.org/browse/authors/f", context = ctx).read()
soup = BeautifulSoup(html)


def avtorji(priimek):
    tag = soup.find_all("h2")
    sez = []


    for e in tag:
        if len(e.find_all("a")) > 0:
        
            seznam_ime = (e.find_all("a")[0].string)
            vrstica = seznam_ime
            seznam_ime = seznam_ime.split(",")
            #print(seznam_ime)
            if priimek == seznam_ime[0]:
                sez.append(vrstica)
    return(sez)
            #print(seznam_ime)

vrne = avtorji("Fairfax")
print(vrne)

