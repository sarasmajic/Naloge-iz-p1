def glajenje(sez):
    seznam = []
    for i in range(len(sez)  - 3):
        vsota = 0
        vsota += sez[i] + sez[i + 1] + sez[i + 2] + sez[i + 3]
        vsota  = vsota / 4

        seznam.append(vsota)
    return seznam

        

vrne = glajenje([3,5,8,0,7,-3,12,0,-5,5])
print(vrne)


#NEDOKONCANA