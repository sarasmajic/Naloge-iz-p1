import unittest
import collections

def dopis(kdo, komu, relacije):
        if kdo not in relacije:
            k = set()
            relacije[kdo] = k
            k.add(komu)
        else:
            relacije[kdo].add(komu)
    
        return(relacije)

def najzgovornejsi(relacije):
    max = -100
    for kljuc in relacije:
        #print(relacije[kljuc]) vrne sete vrednosti
        if len(relacije[kljuc]) > max:
            max = len(relacije[kljuc])
            oseba = kljuc
    return oseba

def vse_osebe(relacije):
    mnozica_oseb = set()
    for kljuc in relacije:
        if kljuc not in mnozica_oseb:
            mnozica_oseb.add(kljuc)

        for vrednosti in relacije[kljuc]:
            if vrednosti not in mnozica_oseb:
                mnozica_oseb.add(vrednosti)
            
    return(mnozica_oseb)

def neznanci(ime, relacije):
    mnozica = set()
    for kljuc in relacije:
    
        for vrednosti in relacije[kljuc]: #cilka berta dani cilka
          
             #print(relacije[ime]) #berta,dani,cilka
                if vrednosti not in relacije[ime]:
                    mnozica.add(vrednosti)
                if kljuc not in relacije[ime] and kljuc != ime:
                    mnozica.add(kljuc)
                else:
                    pass
        
      

    return mnozica 


class TestNajprejLihi(unittest.TestCase):
    def test(self):
        s = [1, 2, 3, 4]
        self.assertIsNone(najprej_lihi(s), "Funkcija ne sme vračati rezultata")
        self.assertListEqual(s, [1, 3, 2, 4])

        s = [4, 3, 2, 1]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [3, 1, 4, 2])

        s = [1, 3, 5]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [1, 3, 5])

        s = [5, 3, 1]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [5, 3, 1])

        s = [2, 4, 6]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [2, 4, 6])

        s = [6, 4, 2]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [6, 4, 2])

        s = [1]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [1])

        s = [2]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [2])

        s = [21, 34]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [21, 34])

        s = [34, 21]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [21, 34])

        s = [34, 34, 21, 34, 21]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [21, 21, 34, 34, 34])


class TestBinarno(unittest.TestCase):
    def test(self):
        self.assertEqual(binarno(3), "11")
        self.assertEqual(binarno(2), "10")
        self.assertEqual(binarno(1), "1")
        self.assertEqual(binarno(0), "0")
        self.assertEqual(binarno(42), "101010")


class TestDopisovanje(unittest.TestCase):
    def test_dopis(self):
        relacije = collections.defaultdict(set)
        dopis("Ana", "Berta", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta"}})
        dopis("Ana", "Berta", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta"}})

        relacije2 = collections.defaultdict(set)
        dopis("Ana", "Cene", relacije2)

        dopis("Ana", "Cilka", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta", "Cilka"}})
        dopis("Berta", "Cilka", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta", "Cilka"},
                                    "Berta": {"Cilka"}})
        dopis("Ana", "Dani", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta", "Cilka", "Dani"},
                                    "Berta": {"Cilka"}})

    def test_najzgovornejsi(self):
        self.assertEqual(najzgovornejsi({"Ana": {"Berta", "Cilka", "Dani"},
                                         "Berta": {"Cilka"}}),
                         "Ana")
        self.assertEqual(najzgovornejsi({"Berta": {"Cilka"}}),
                         "Berta")
        self.assertEqual(najzgovornejsi({"Ana": {"Berta", "Cilka", "Dani"},
                                         "Berta": {"Cilka"},
                                         "Cilka": {},
                                         "Ema": {"Cilka", "Fanci", "Greta",
                                                 "Helga"}}),
                         "Ema")

    def test_vse_osebe(self):
        self.assertSetEqual(vse_osebe({"Ana": {"Berta", "Cilka", "Dani"},
                                       "Berta": {"Cilka"}}),
                            {"Ana", "Berta", "Cilka", "Dani"})
        self.assertSetEqual(vse_osebe({"Ana": {"Berta", "Dani"},
                                       "Berta": {"Cilka"}}),
                            {"Ana", "Berta", "Cilka", "Dani"})
        self.assertSetEqual(vse_osebe({"Ana": {"Berta"}}),
                            {"Ana", "Berta"})
        self.assertSetEqual(vse_osebe({"Ana": set()}),
                            {"Ana"})
        self.assertSetEqual(vse_osebe({}),
                            set())

    def test_neznanci(self):
        relacije = {"Ana": {"Berta", "Cilka", "Dani"},
                    "Berta": {"Cilka"},
                    "Cilka": set(),
                    "Ema": {"Cilka", "Fanci", "Greta"}}
        self.assertFalse("Ana" in neznanci("Ana", relacije),
                         "Nobena oseba ni neznana sebi")
        self.assertSetEqual(neznanci("Ana", relacije),
                            {"Ema", "Fanci", "Greta"})
        self.assertSetEqual(neznanci("Berta", relacije),
                            {"Ana", "Dani", "Ema", "Fanci", "Greta"})
        self.assertSetEqual(neznanci("Cilka", relacije),
                            {"Ana", "Berta", "Dani", "Ema",
                             "Fanci", "Greta"})
        self.assertSetEqual(neznanci("Ema", relacije),
                            {"Ana", "Berta", "Dani"})


class TestZapor(unittest.TestCase):
    def test_sogovorniki(self):
        self.assertEqual(sogovorniki([["ABC", "B", "BC", "E", "A"],
                                      ["C", "D", "AE", "DB", "DC"],
                                      ["BC", "AE", "E", "BC", "AED"]]), 9)
        self.assertEqual(sogovorniki([["ABC", "B", "BC", "E", "A"]]), 2)
        self.assertEqual(sogovorniki([["ABC", "B", "BCA", "A"]]), 3)
        self.assertEqual(sogovorniki([["ABC"], ["C"], ["BC"]]), 2)
        self.assertEqual(sogovorniki([["ABC"]]), 0)
        self.assertEqual(sogovorniki([["ABC", "DE", "BC"]]), 0)
        self.assertEqual(sogovorniki([["ABC"], ["DE"], ["BC"], ["A"]]), 0)


class TestBlok(unittest.TestCase):
    def test_konstruktor(self):
        blok = Blok(3)

    def test_vseli(self):
        blok = Blok(3)
        blok2 = Blok(5)
        self.assertTrue(blok.vseli(1, "Ana"))
        self.assertTrue(blok.vseli(2, "Berta"))
        self.assertFalse(blok.vseli(1, "Cilka"))
        self.assertFalse(blok.vseli(1, "Ana"))
        self.assertTrue(blok.vseli(0, "Ana"))
        self.assertTrue(blok2.vseli(1, "Berta"))

    def test_stanovalec(self):
        blok = Blok(20)
        blok2 = Blok(5)
        for i in range(20):
            self.assertIsNone(blok.stanovalec(i))
        self.assertTrue(blok.vseli(18, "Ana"))
        self.assertEqual(blok.stanovalec(18), "Ana")
        self.assertTrue(blok.vseli(2, "Berta"))
        self.assertEqual(blok.stanovalec(18), "Ana")
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertFalse(blok.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertIsNone(blok.stanovalec(1), "Berta")

        self.assertTrue(blok2.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertEqual(blok2.stanovalec(2), "Cilka")

    def test_izseli(self):
        blok = Blok(20)
        self.assertTrue(blok.vseli(18, "Ana"))
        self.assertEqual(blok.stanovalec(18), "Ana")
        self.assertTrue(blok.vseli(2, "Berta"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertFalse(blok.vseli(2, "Berta"))
        self.assertFalse(blok.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertIsNone(blok.izseli(2),
                          "Metoda 'izseli' naj ne vrača rezultata")
        self.assertIsNone(blok.stanovalec(2))
        self.assertTrue(blok.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Cilka")

    def test_kamorkoli(self):
        blok = Blok(5)
        blok.vseli(2, "Ana")
        self.assertTrue(blok.kamorkoli("Berta"))
        self.assertIsNone(blok.stanovalec(0))
        self.assertIsNone(blok.stanovalec(1))
        self.assertEqual(blok.stanovalec(2), "Ana")
        self.assertIsNone(blok.stanovalec(3))
        self.assertEqual(blok.stanovalec(4), "Berta")
        self.assertTrue(blok.kamorkoli("Cilka"))
        self.assertEqual(blok.stanovalec(3), "Cilka")
        self.assertFalse(blok.vseli(3, "Dani"))
        self.assertEqual(blok.stanovalec(3), "Cilka")
        self.assertTrue(blok.kamorkoli("Dani"))
        self.assertTrue(blok.kamorkoli("Ema"))
        self.assertEqual(blok.stanovalec(0), "Ema")
        self.assertEqual(blok.stanovalec(1), "Dani")
        self.assertEqual(blok.stanovalec(2), "Ana")
        self.assertEqual(blok.stanovalec(3), "Cilka")
        self.assertEqual(blok.stanovalec(4), "Berta")
        self.assertFalse(blok.kamorkoli("Fanci"))

if __name__ == "__main__":
    unittest.main()
