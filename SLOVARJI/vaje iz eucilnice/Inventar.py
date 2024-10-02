inv = {'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}

def zaloga(inventar, artikel):
    if artikel in inventar:
        return(inventar[artikel])
    
vrne = zaloga(inv, "makovka")
print(vrne)

def prodaj(inventar, artikel, kolicina):
    if artikel in inventar:
        inventar[artikel] = inventar[artikel] - kolicina
    return inventar

vrne = prodaj(inv, "makovka", 3)
print(vrne)

def primanjkljaj(inventar, narocilo):
    slovar = {}
   
    for key_nar, value_nar in narocilo.items():
        if key_nar not in inventar:
            slovar[key_nar] = value_nar
        else:
            if value_nar > inventar[key_nar]:
                razlika = value_nar - inventar[key_nar]
                slovar[key_nar] = razlika

    return(slovar)

vrne = primanjkljaj(inv, {"pašteta": 3, "klobasa": 9, "pivo": 1})
print(vrne)

