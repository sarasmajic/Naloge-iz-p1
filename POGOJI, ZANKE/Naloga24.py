def bomboni(s):
    max = -100000
    skupno = 0

    for e in s:
        if e > max:
            max = e

    for e in s:
        st_bombonov = max - e
        skupno += st_bombonov
    #print(skupno)
           
    
    #print(st_bombonov)
    
    return skupno

vrne = bomboni([5, 8, 6, 4])
print(vrne)
