def freq(s):
    slovar = {}

    for crka in s:
        if crka not in slovar:
            slovar[crka] = 1
        else:
            slovar[crka] += 1
    return slovar

vrne = freq("abcaad")
print(vrne)


def max_freq(f):
    max = -100
    for key, value in f.items():
        if max < value:
            max = value
            iskan_kljuc = key
    return iskan_kljuc

vrne = max_freq({'a': 3, 'b': 1, 'c': 1, 'd': 1})
print(vrne)

#vecinoma nalog je v pdf zbirki resenih nalog