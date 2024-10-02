def sumljive(stavek):
    seznam = []
    nov_seznam = []


    besede = stavek.split(" ")
    for beseda in besede:
        seznam.append(beseda)

    for e in seznam:   #lahko bi tudi brez seznama, sploh ni potreben, naredila sem ga za vajo
        if "a" in e and "u" in e:
            nov_seznam.append(e)
    return nov_seznam
   


vrne = sumljive('Muh pa je rekla: "Tale juha se je pa res prilegla, najlepsa huala," in odletela.')
print(vrne)