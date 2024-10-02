def najvecji_abs(s):
    min = -10000
    for e in s:
        absolutna_cifra = abs(e)
        if absolutna_cifra > min:
            min = absolutna_cifra
    
    return min

vrne = najvecji_abs([-5, -8, 3, -12, 15])
# predstavljaj si, da se zgornja vrstica spremeni v
# vrne = 15
print(vrne)



#x = abs(-7.25)
#print(x)