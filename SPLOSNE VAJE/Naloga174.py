def brez_ntih(s,n):
    for i in range(len(s)):
        #print(s[i])
        cifra = i + 3 #gre za dva naprej
        print(cifra, s[i])

       # if s[i] % n == 0:
        #    s.remove(s[i])
        #print(cifra)


vrne = brez_ntih([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
print(vrne) 