from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen("https://www.gutenberg.org/browse/authors/b", context = ctx).read()



#ids = {"sara": 10, "gregor": 3}
#print(ids["sara"])


soup = BeautifulSoup(html)
author_tag = soup.find_all("h2")
slovar = {}

for e in author_tag: 
    #print(e.string)
    #print(e.find_all("a"))
    if len(e.find_all("a")) > 0:

        #print(e.find_all("a")[1].attrs["href"])

        string_ime = e.find_all("a")[0].string
        #print(string_ime)
        atributi_slovar = e.find_all("a")[0].attrs
        #print(e.find_all("a")[0].attrs) {'name': 'a4193'}
        id = atributi_slovar["name"]

        if string_ime not in slovar:
            slovar[string_ime] = id
        
print(slovar)


    #linki = e.find_all("a")[0].string
    

    #string = string.split(",") 
    #string = string[:-1]
    #print(string)

    #<tag id="adfasdf" class="dfadf"> string </tag>
