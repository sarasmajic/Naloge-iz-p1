#Izpiši, kateri predmet je dosegel najvišjo ceno, kdo ga je kupil in za koliko.
#Izpiši končne cene vseh predmetov (vsak predmet v drugi vrstici).
#Izpiši, koliko ponudb je bil deležen vsak izmed predmetov (vsak v drugi vrstici).
#Izpiši, za kateri predmet je bilo največ ponudb. Če si prvo mesto deli več izdelkov, izpiši enega od njih.

#1
seznam = []
max = -10000

for vrstica in open("zapisnik.txt"):
    vrstica = vrstica.strip()
    vrstica = vrstica.split(",")
    vrstica[2] = int(vrstica[2])

    if max < vrstica[2]:
        max = vrstica[2]
        oseba = vrstica[1]
        predmet = vrstica[0]

print("Najdrazji predmet je ", predmet, "- za ", max, "ga je kupila", oseba)

#2
slovar = {}

for vrstica in open("zapisnik.txt"):
    vrstica = vrstica.strip()
    vrstica = vrstica.split(",")
    vrstica[2] = int(vrstica[2])

    if vrstica[0] not in slovar:
        slovar[vrstica[0]] = [vrstica[2]]
    else:
        slovar[vrstica[0]].append(vrstica[2])

for kljuc in slovar:
    print(kljuc, slovar[kljuc][-1])


#3
max_ponudb = -100
slovar2 = {}
for vrstica in open("zapisnik.txt"):
    vrstica = vrstica.strip()
    vrstica = vrstica.split(",")
    vrstica[2] = int(vrstica[2])

    if vrstica[0] not in slovar2:
        slovar2[vrstica[0]] = 1
    else:
        slovar2[vrstica[0]] += 1

print(slovar2)

#4
for key, value in slovar2.items():
    if value > max_ponudb:
        max_ponudb = value
        max_predmet = key
print(max_predmet, max_ponudb)


#dodatna naloga
#Za vsako osebo izpiši, koliko je porabila na dražbi.
#Za vsak izdelek izpiši, za koliko je bila končna cena višja od prve.

#4
slovar3 = {}
for vrstica in open("zapisnik.txt"):
    vrstica = vrstica.strip()
    vrstica = vrstica.split(",")
    vrstica[2] = int(vrstica[2])

    if vrstica[1] not in slovar3:
        slovar3[vrstica[1]] = vrstica[2]
    else:
        slovar3[vrstica[1]] += vrstica[2]

print(slovar3)
print()
#5
slovar4 = {}
for vrstica in open("zapisnik.txt"):
    vrstica = vrstica.strip()
    vrstica = vrstica.split(",")
    vrstica[2] = int(vrstica[2])

    if vrstica[0] not in slovar4:
        slovar4[vrstica[0]] = [vrstica[2]]
    else:
        slovar4[vrstica[0]].append(vrstica[2])


#6
for kljuc in slovar4:
    if len(slovar4[kljuc]) > 0:
        #print(slovar4[kljuc][0])
        razlika2 = (slovar4[kljuc][-1] - slovar4[kljuc][0])
    else:
        razlika2 = 0

    print(kljuc, razlika2)
    
   # print((value))
   
        


