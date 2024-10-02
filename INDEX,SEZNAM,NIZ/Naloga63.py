def zmagovalec(s):

    i = 0 #je kazalec na kateri osebi smo
    while len(s) > 1:
        for j in range(10): #11x
            i += 1
            if len(s) == i:
                i = 0
        #print(s[i])
        s.pop(i)

    return s[0]

vrne = zmagovalec(["Maja", "Janja", "Sabina", "Ina", "Jasna"])
print(vrne)


"""def vsota(seznam):
    if len(seznam) == 0:
        return 0
    else:
        return seznam[0] + vsota(seznam[1:])
    

print(vsota([1, 2, 3]))


exit()"""
