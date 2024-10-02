str_stizd = input("Stevilo izdelkov: ")
st_izd = int(str_stizd)
vsota = 0

for x in range(st_izd):
    vnos = input("cena izdelka: ")
    int_vnos = int(vnos)
    vsota += int_vnos

print(vsota)