def transakcije(zacetek, dajatve):
    for e1 in zacetek:
        oseba = e1[0]
        zlatniki_na_zacetku = e1[1]
        
        for e2 in dajatve:
            daje = e2[0]
            dobi = e2[1]
            kolicina_dajatve = e2[2]

            
            
        



vrne = transakcije([('Ana', 4), ('Berta', 8), ('Cilka', 10)], [('Cilka', 'Ana', 3), ('Cilka', 'Ana', 2), ('Ana', 'Berta', 2)])
print(vrne)