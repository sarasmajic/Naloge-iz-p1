def skalarni(v, w):
    vsota = 0
    for i in range(3):
        rezultat = v[i] * w[i]
        vsota += rezultat
    return vsota





vrne = skalarni((1, 2, 3), (5, 4, 6))
print(vrne)

#for i in range(1, 1000):
#d    print("I love you")