inv = {'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}
    
def zaloga(inventar, izdelek):
    for kljuc, vrednost in inv.items():
        if kljuc == izdelek:
            return vrednost


vrne = zaloga(inv, "makovka")
print(vrne)

def prodaj(inventar, izdelek, kolicina):
    for key, value in inv.items():
        if key == izdelek:
            inv[key] = value - kolicina 
            print(inv)

vrne = prodaj(inv, "makovka", 3)
print(vrne)


narocilo_slovar = {"pašteta": 3, "klobasa":9, "pivo": 1}
def primanjkljaj(inventar, narocilo):
    nov_slovar = {}
    for ki, vi in inv.items():
        for kn, vn in narocilo_slovar.items():
            if kn not in inv:
                nov_slovar[kn] = vn
            
            razlika = 0
            if kn == ki:
                if vn > vi:
                    razlika = vn - vi
                    nov_slovar[kn] = razlika
    
                    return nov_slovar




vrne = primanjkljaj(inv, narocilo_slovar)
print(vrne)