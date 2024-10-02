from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen("https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_si_latest.html", context = ctx).read()
soup = BeautifulSoup(html)

author_tag = soup.find_all("tr")
#print(author_tag)

slovar = {}

for e in author_tag:
    if len(e.find_all("td")) > 0:
        temp = e.find_all("td")[3].string
        cela_vrstica = e.find_all("td")[0].string
        


        if cela_vrstica not in slovar:
            slovar[cela_vrstica] = temp
print(slovar)
        


