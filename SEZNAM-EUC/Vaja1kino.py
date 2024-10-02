filmi = [
    ('Poletje v skoljki 2', 6.1), 
    ('Ne cakaj na maj', 7.3), 
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1), 
    ('Poletje v skoljki', 7.2), 
    ('To so gadi', 7.7), 
]

#imena vseh filmov z oceno vsaj 7,0,
for e in filmi:
    ocena = e[1]
    if ocena > 7.0:
        print(e[0])
print()

#ime filma z najvišjo oceno,
max = 0
for e in filmi:
    ocena = e[1]
    film = e[0]
    if ocena > max:
        max = ocena
        max_film = film

print(max_film)
print()

#povprečno oceno vseh filmov v seznamu,
vsota = 0
stevec = 0
for e in filmi:
    ocena = e[1]
    film = e[0]


    vsota += ocena
    stevec += 1

    povprecje = vsota / stevec
print(povprecje)
print()


#ime prvega filma v seznamu z oceno vsaj 7,0.
for e in filmi:
    oc = e[1]
    fi = e[0]
    if oc > 7.0:
        break
print(fi)