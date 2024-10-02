import numpy as np

#stevilo vseh prodanih predmetov
cene = np.genfromtxt("drazba.txt", dtype=int) #ker je txt file v istemu folderju kokr ta naloga(zagnala se bo)
index = (cene == -1) 

print(cene)
#vecje = (cene > 10) #v seznam shrani True/False (true ce je vecja kot 10)
#print(vecje)

#print(np.average(cene[vecje])) #funkcija za povprecje, cene[vecje] --> vrne array stevil ki so vecje od 10
#np.mean = np.average

#print(np.sum(cene)) #vrne vsoto vseh stevil

print(np.sum(index))

#2
print(np.max(cene))

#3
i = 0
vsota = 0
for i in range(len(cene)):
    if cene[i] == -1:
        vsota = vsota + cene[i - 1]
print(vsota)


    