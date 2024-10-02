def st_ujemanj(b1,b2):
    l1 = len(b1)
    l2 = len(b2)

    l = 0
    if l1 < l2:
        l = l1
    else:
        l = l2

    stevec = 0 # st. enakih crk

    for i in range(l):
        b1[i] # i-ta črka b1
        b2[i] # i-ta črka b2

        if b1[i] == b2[i]:
            stevec += 1

    return stevec
vrne = st_ujemanj("PAV", "KRVAVICA")
print(vrne)