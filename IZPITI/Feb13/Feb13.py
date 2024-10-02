#1 tovornjaki, kolk vozenj je potrebnih
def tovorjnaki(omare):
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
        
        

vrne = tovorjnaki([])
print(vrne)


