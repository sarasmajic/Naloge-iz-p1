def posrednik(s):
    zacetna_vrednost = 0
    max = -10000000
    min = 10000000
    for i in range(len(s)):
        #print(s[i]) -- da element
        zacetna_vrednost = zacetna_vrednost + s[i]
        #print(zacetna_vrednost)
        if zacetna_vrednost > max:
            max = zacetna_vrednost
        
            for ind in range(len(s)):
                print(ind)

        
        
        if zacetna_vrednost < min:
            min = zacetna_vrednost
            indeks = i
    
    print(min, indeks)
   # print(max)
        


vrne = posrednik([1, -2, -4, 1, 2, -1, 3, 4, -2, 1, -5, -5])
print(vrne)
# (0) --- 1, -1, -5, -4, -2, -3, 