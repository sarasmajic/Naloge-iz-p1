import math #importamo math library za sin

hitrost = input("hitrost?")
hitrost = int(hitrost) #jih pretvorimo iz str -- v int

kot = input("kot?")
kot = int(kot) #pretvorba iz str v int
kot_rad = (kot * math.pi/180)
#print(kot_rad) preverimo če smo pravilno pretvorili

s = (hitrost**2) * (math.sin(2* kot_rad)) / 9.807
print(s)

#komentar:
#pri nalogi se zna zgoditi da je razdalja negativna, kar ni pravilno .. do tega pride saj funckija sinus avtomaticno
#dobi notr kot v radijih, tako da je treba kot v stopinjah najprej spremeniti v radije