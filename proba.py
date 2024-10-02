def evidenca(postavke, ime_datoteke):
    #print(postavke[0]) vrne prov prvo terko

    f = open(ime_datoteke, "w")

    f.write(f"{'Stvar':6}{'Cena X Kosov':>20}{'Skupaj':>20}\n")
    f.write("-" * (6 + 40) + "\n")

    for p in postavke:
        vsota = 0
        predmet = p[0]
        cena = p[1]
        kos = p[2]
        vsota = cena * kos
        f.write(f"{predmet:<8}{cena:>10}{'x':>2}{kos:>3}{vsota:>23}\n")

    

vrne = evidenca([("slika", 50, 2),("tempera", 3, 1),("stol", 20, 1),("kip", 20, 12),("zrak", 0, 141),("torba", 12, 1)], "Jan1-24-zapis.txt")
print(vrne)
