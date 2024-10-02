from random import randint, choice
import unittest

# Razred, ki ga uporabljate v nalogah 4 in 5
# Razred je takšen, kot je, in ga ne smete spreminjati

#1 tovornjaki, kolk vozenj je potrebnih
def tovornjaki(omare):
    vsota = 0
    stevec = 1

    if len(omare) == 0:
        return 0

    for i in range(len(omare)):
        vsota += omare[i]
        if vsota > 2000:
            stevec += 1
            vsota = omare[i]
    return stevec
        
        


class Tocka(list):
    def soseda(self, kam):
        return Tocka(self[kam=="J"])

    def konec(self):
        return len(self) == 1

    def znak(self):
        return self[0]


# Testi za nalogo 1

class Tovornjaki(unittest.TestCase):
    def test(self):
        self.assertEqual(tovornjaki([1500, 1000, 200, 900]), 3,
            "Prvi primer izmed onih ob besedilu naloge ne deluje")
        self.assertEqual(tovornjaki([1500, 500]), 1,
            "Obe omari, 1500 in 500 gresta na isti tovornjak")
        self.assertEqual(tovornjaki([1500, 600]), 2,
            "Druga omara ne more več na prvi tovornjak, potrebujemo dva")
        self.assertEqual(tovornjaki([2000]), 1,
            "Ena dvotonska omara ravno gre na tovornjak")
        self.assertEqual(tovornjaki([10]), 1,
            "Ena lahko omara, 10 kg, zahteva en tovornjak")
        self.assertEqual(tovornjaki([2000, 2000, 2000]), 3,
            "Tri dvotonske omare zahtevajo tri tovornjake")
        self.assertEqual(tovornjaki([1001, 1001, 1001, 1001, 1001, 1001]), 6,
            "Šest omar po 1001 kg zahteva šest tovornjakov")
        self.assertEqual(tovornjaki([1800, 100]), 1,
            "Omari po 1800 in 100 gresta brez težav na en tovornjak")
        self.assertEqual(tovornjaki([1800, 100, 101]), 2,
            "Tri omare in tretja mora ravno za las na novega")
        self.assertEqual(tovornjaki([1800, 200, 101]), 2,
            "Tri omare; dve točno prideta na enega, tretja zahteva novega")
        self.assertEqual(tovornjaki([]), 0,
            "Če ni omar, ne potrebujemo tovornjakov")

t = Tovornjaki()
t.test()
# Testi za nalogo 2

class Pajek(unittest.TestCase):
    def test(self):
        self.assertEqual(pajek([(-2, 0)]), 1, "Narobe: enkrat čez os y")
        self.assertEqual(pajek([(2, 0), (-1, -2), (1, -1), (-5, 5)]), 3,
            "Narobe: najprej ne prečka ničesar, nato x, nato nič, nato obe")
        self.assertEqual(pajek([(1, 5), (2, 1), (5, 1), (1, 3)]), 0,
            "Pajek, ki rine le gor in desno, ne bo nikoli prečkal ničesar")
        self.assertEqual(pajek([]), 0,
            "Pajek, ki ne gre nikamor, ne prečka ničesar")


# Testi za nalogo 3

class Soimenjaki(unittest.TestCase):
    def test(self):
        def s(d):
            return {k: sorted(v) for k, v in d.items()}

        self.assertEqual(s(soimenjaki("studenti1")),
            {'Janez Novak': ['63152568', '63155912'],
             'Matija Kralj': ['63153650', '63153962', '63154189']})

        self.assertEqual(s(soimenjaki("studenti2")),
            {'Janez Novak': ['63152730', '63154624']})

        self.assertEqual(s(soimenjaki("studenti3")), {})

        self.assertEqual(s(soimenjaki("studenti4")), {})



# Testi za nalogo 4

# tocka1 predstavlja gornjo levo tocko zemljevida, ki je podan kot primer
# na izpitni poli
tocka1 = Tocka([[[["I", "L"], ["N", [["J", "K"], ["B", "Č"]]]],
                 ["A", ["O", ["M", "R"]]]],
                [["F", [[".", "Ž"], ["T", "U"]]], ["P", ["D", "E"]]]])

# tocka2 predstavlja tocko zemljevida, v katerem vodita iz prve tocke le dve
# poti: na koncu vzhodne je A, na koncu zahodne B

tocka2 = Tocka(["A", "B"])


class Branje(unittest.TestCase):
    def test_crka_na_tocka1(self):
        self.assertEqual(crka(tocka1, "JVV"), ("F", ""))
        self.assertEqual(crka(tocka1, "JVVJVV"), ("F", "JVV"))
        self.assertEqual(crka(tocka1, "VVVV"), ("I", ""))
        self.assertEqual(crka(tocka1, "VVVVV"), ("I", "V"))
        self.assertEqual(crka(tocka1, "JVJJJVVVV"), ("U", "VVVV"))
        self.assertEqual(crka(tocka1, "JVJJJJJJJ"), ("U", "JJJJ"))

    def test_crka_na_tocka2(self):
        self.assertEqual(crka(tocka2, "V"), ("A", ""))
        self.assertEqual(crka(tocka2, "VJJ"), ("A", "JJ"))
        self.assertEqual(crka(tocka2, "VVV"), ("A", "VV"))
        self.assertEqual(crka(tocka2, "J"), ("B", ""))
        self.assertEqual(crka(tocka2, "JJJJJJ"), ("B", "JJJJJ"))
        self.assertEqual(crka(tocka2, "JVVVVV"), ("B", "VVVVV"))

    def test_preberi_na_izmisljenem(self):
        for i in range(10):
            a, b, c, d = (chr(randint(0, 31)) for i in range(4))
            tocka = Tocka([[a, b], [c, d]])
            self.assertEqual(crka(tocka2, "VVV"), (a, "V"))
            self.assertEqual(crka(tocka2, "VJJ"), (b, "J"))
            self.assertEqual(crka(tocka2, "JVJ"), (c, "J"))
            self.assertEqual(crka(tocka2, "JJV"), (d, "V"))

    def test_preberi_na_tocka1(self):
        self.assertEqual(preberi(tocka1, "JVV"), "F")
        self.assertEqual(preberi(tocka1, "JVVJVVJVVJVV"), "FFFF")
        self.assertEqual(preberi(tocka1, "JVVVJJJJVVVV"), "FRI")
        self.assertEqual(preberi(tocka1,
            "JJVVJVVVVJVJVVVJJJJVVVVVVJVVVJJVJVJV"), "PALAČINKA")
        self.assertEqual(preberi(tocka1,
            "VVJJVVJVJJJJVJJVVJJJJVVVV"), "JUTRI")

    def test_preberi_na_tocka2(self):
        for i in range(10):
            pot = "".join(choice("JV") for i in range(randint(2, 10)))
            rezultat = pot.replace("V", "A").replace("J", "B")
            self.assertEqual(preberi(tocka2, pot), rezultat,
                "pot {} da niz {}".format(pot, rezultat))

    def test_preberi_na_izmisljenem(self):
        for i in range(5):
            a, b = chr(randint(0, 31)), chr(randint(0, 31))
            tocka = Tocka([a, b])
            for i in range(10):
                pot = "".join(choice("JV") for i in range(randint(2, 10)))
                rezultat = pot.replace("V", a).replace("J", b)
                self.assertEqual(preberi(tocka, pot), rezultat,
                    "funkcija ne deluje, če si izmislim kake čudne znake".
                    format(pot, rezultat))


# Testi za nalogo 5

class Huffman(unittest.TestCase):
    def test(self):
        self.assertDictEqual(huffman(tocka1),
            {'A': 'VJV', 'F': 'JVV', 'B': 'VVJJJV', 'Č': 'VVJJJJ', 'D': 'JJJV',
             'I': 'VVVV', 'K': 'VVJJVJ', 'J': 'VVJJVV', 'M': 'VJJJV',
             'L': 'VVVJ', 'O': 'VJJV', 'N': 'VVJV', 'P': 'JJV', 'R': 'VJJJJ',
             'U': 'JVJJJ', 'T': 'JVJJV', 'E': 'JJJJ', '.': 'JVJVV',
             'Ž': 'JVJVJ'})

        self.assertDictEqual(huffman(tocka2),
            {'A': 'V', 'B': 'J'})

        for i in range(10):
            a, b, c, d = (chr(randint(0, 31)) for i in range(4))
            tocka = Tocka([[a, b], [c, d]])
            self.assertDictEqual(huffman(tocka),
                {a: "VV", b: "VJ", c: "JV", d: "JJ"})

            tocka = Tocka([[[a, b], c], d])
            self.assertDictEqual(huffman(tocka),
                {a: "VVV", b: "VVJ", c: "VJ", d: "J"})

            tocka = Tocka([a, [b, [c, d]]])
            self.assertDictEqual(huffman(tocka),
                {a: "V", b: "JV", c: "JJV", d: "JJJ"})


