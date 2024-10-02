def primerjava(vz, bes):
    for i in range(len(vz)):
        if len(bes) > len(vz) or len(bes) < len(vz):
            return False
        else:
            if vz[i] == ".":
                continue
            else:
                if vz[i] == bes[i]:
                    continue
                else:
                    return False
    return True

vrne = primerjava("r.k.", "reka")
print(vrne)


def krizanka(vzorec, besede):
    seznam = []
    for beseda in besede:
        if primerjava(vzorec, beseda) == True:
            seznam.append(beseda)

    return(seznam)

vrne = krizanka("r.k.", ["reka", "rokav", "robot", "roka"])
print(vrne)