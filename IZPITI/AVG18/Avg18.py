def stisni(s):
    seznam = []
    vsota = 1
    string = ""

    if len(s) == 0:
        return ("")
    else:

        for i in range(len(s) - 1):
            
            if s[i] == s[i + 1]:
                vsota += 1
            else:
                #print(str(vsota),s[i])
                string += str(vsota) + s[i] + " "
                vsota = 1

    #return string
    string += str(vsota) + s[-1]
    return string
        #print(s[i + 1], vsota)


vrne = stisni("")
print(vrne)

def razsiri(s):
    izpis = ""

    if len(s) == 0:
        return ("")
    
    s = s.split(" ")
    for e in s:
        st = int(e[:-1])
        crka = e[-1]
        string = st * crka

        izpis += string
    print(izpis)

        #print(e)
        
vrne = razsiri("")
print(vrne)

#2 lzw
def lzw_stisni(s, kode):
    string = ""

    for crka in s:
        if crka in kode:
            string += kode[crka]
    return string
            

vrne = lzw_stisni("DAVID", {"E": "00", "A": "01", "I": "10", "D": "110", "V": "111"})
print(vrne)

def lzw_razsiri(s, kode):
    for i in range(len(s)):
        if s[i: i +2] != kode[s]:
            print(s[i])


vrne = lzw_razsiri("1100111110110", {"D": "110", "A": "01", "E": "00", "V": "111", "I": "10"})
print(vrne)
