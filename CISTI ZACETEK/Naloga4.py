import math

vnos = input("Dolžine stranic: ")
stranica = vnos.split(" ")
stranica[0] = int(stranica[0])
stranica[1] = int(stranica[1])
stranica[2] = int(stranica[2])

if stranica[0] + stranica[1] < stranica[2] or stranica[1] + stranica[2] < stranica[0] or stranica[2] + stranica[0] < stranica[1]:
    print("Tak trikotnik ne obstaja")

else:   

    s = (stranica[0] + stranica[1] + stranica [2]) / 2

    ploscina = math.sqrt(s * (s - stranica[0]) * (s - stranica[1]) * (s - stranica[2]))
    print (ploscina)

def ploscina_trikotnika(a, b, c):
    s1 = (a + b + c) / 2
    ploscina1 = math.sqrt(s* (s -a) * (s - b) (s - c))
    return ploscina1

vrne = ploscina_trikotnika(stranica[0], stranica [1], stranica[2])
print(vrne)

