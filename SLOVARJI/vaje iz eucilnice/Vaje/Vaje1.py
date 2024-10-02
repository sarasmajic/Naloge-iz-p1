#vaje iz slovarjev iz eucilnice  (vremenske-postaje.txt)

#najvisja in najnizja temperatura

max = -10000
min = 100000

for vrstica in open("vremenske-postaje.txt"):
    kraj, datum, najvisja, najnizja = vrstica.split(",")
    najvisja = int(najvisja)
    najnizja = int(najnizja)

    if najvisja > max:
        max = najvisja
    
    if min > najnizja:
        min = najnizja
    
print(max)
print(min)
#print(najnizja)

