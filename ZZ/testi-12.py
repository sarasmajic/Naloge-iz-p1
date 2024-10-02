
def knjigovodstvo(ime_datoteke):
    seznam_poz = []
    seznam_neg = []
    vsota = 0

    for vrstica in open(ime_datoteke):
        vrstica = vrstica.strip()
        vrstica = vrstica.split(":")
        vrstica[1] = int(vrstica[1])
   

        if vrstica[1] > 0:
            seznam_poz.append((vrstica[0], vrstica[1]))
        if vrstica[1] < 0:
            #vrstica[1] = abs(vrstica[1]) nesmes tuki ker potem se dol prenese in vsote ne izracuna prov
            seznam_neg.append((vrstica[0], abs(vrstica[1])))


        vsota += vrstica[1] 
    return(seznam_poz, seznam_neg, vsota)


def draginja(odhodki):
    slovar = {}
    max = -100

    for terka in odhodki:
        predmet = terka[0]
        cena = terka[1]
        if predmet not in slovar:
            slovar[predmet] = [cena]
        else:
            slovar[predmet].append(cena)
    
    for key, value in slovar.items():
        vsota = sum(value)
        povprecje = vsota / len(value)
        if povprecje > max:
            max = povprecje
            pred = key
            
    return pred
        #print(key, povprecje)
        #print(key, value)



import unittest
import warnings

with open("knjigovodstvo.txt", "w", encoding="utf-8") as f:
    f.write("""slika: 50
slika: 100
tempera: -3
stol: -20
kip: 20
zrak: 0
torba: 12
""")

with open("knjigovodstvo.html", "w", encoding="utf-8") as f:
    f.write("""<html>
    <head>
    <title>Knjigovodstvo</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style>
    dt { font-weight: bold; }
    dd { margin-left: 1em; }
    </style>
    </head>
    <body>
    <p>V tem letu smo kupili:</p>
    <dl>
        <dt>slika</dt>
        <dd>Stala je 50, lahko bi tudi malo manj.</dd>
        <dt>slika</dt>
        <dd>Ta je bila malo dražje, zanjo smo dali 100.</dd>
        <dt>tempera</dt>
        <dd>Kdo bi si mislil, da so že po 3 cekine!</dd>
        <dt>polomljen stol</dt>
        <dd>Za 20. Samo!</dd>
        <dt>kip</dt>
        <dd>Čuden, ne vem,
        zakaj je stal 20.</dd>
        <dt>zrak</dt>
        <dd>Je zastonj, torej stane 0.</dd>
        <dt>torba</dt>
        <dd>Z zadrgo. Za samo 12! V Intersportu.</dd>
    </dl>
    <p>Hvala za pozornost in nasvidenje.</p>
    </body>
""")

class Tests(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_01_knjigovodstvo(self):
        self.assertEqual(
            ([('slika', 50), ('slika', 100), ('kip', 20), ('torba', 12)],
             [('tempera', 3), ('stol', 20)],
             159),
            knjigovodstvo("knjigovodstvo.txt"))

    def test_02_draginja(self):
        self.assertEqual(
            "miza",
            draginja([('stol', 20), ('torba', 12), ('tempera', 3),
                      ('miza', 50), ('stol', 30), ('stol', 60),
                      ('miza', 40), ('torba', 5)]))

    def test_03_dragocenosti(self):
        stvari = np.array(["tempera", "stol", "kip", "zrak", "torba", "slika"])
        cene_po_dnevih = np.random.randint(0, 100, (6, 10))
        cene_po_dnevih[1, 5] = 120
        cene_po_dnevih[2, 2] = 100
        cene_po_dnevih[1, 8] = 130
        cene_po_dnevih[4, 1] = 200
        cene_po_dnevih[5, 1] = 110
        cene_po_dnevih[5, 2] = 120

        self.assertEqual(
            ["stol", "torba", "slika"],
            list(dragocenosti(stvari, cene_po_dnevih, 100)))
        self.assertEqual(
            ["stol", "torba"],
            list(dragocenosti(stvari, cene_po_dnevih, 120)))
        self.assertEqual(
            ["torba"],
            list(dragocenosti(stvari, cene_po_dnevih, 150)))
        self.assertEqual(
            [],
            list(dragocenosti(stvari, cene_po_dnevih, 200)))

    def test_04_spletno_knjigovodstvo(self):
        self.assertEqual(
            [('slika', 50), ('slika', 100), ('tempera', 3), ('polomljen stol', 20),
             ('kip', 20), ('zrak', 0), ('torba', 12)],
            spletno_knjigovodstvo("knjigovodstvo.html"))

    def test_05_evidenca(self):
        postavke = [("slika", 50, 2), ("tempera", 3, 1), ("stol", 20, 1),
                    ("kip", 20, 12), ("zrak", 0, 141), ("torba", 12, 1)]
        evidenca(postavke, "evidenca.txt")
        self.assertEqual("""
Stvar        Cena x Kosov     Skupaj
------------------------------------
slika          50 x 2            100
tempera         3 x 1              3
stol           20 x 1             20
kip            20 x 12           240
zrak            0 x 141            0
torba          12 x 1             12
""".strip(), open("evidenca.txt", encoding="utf-8").read().strip())


if __name__ == '__main__':
    unittest.main()
