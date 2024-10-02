from random import *
a = randint(2, 10) #a je prva cifra, b je druga cifra
b = randint(2, 10)

print(a, "krat", b)
vnos = input("Odgovor? ")
int_vnos = int(vnos)

if a*b == int_vnos:
    print("Pravilno")

else:
   print("Napačno")
