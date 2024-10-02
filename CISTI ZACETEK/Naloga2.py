import math

vnos = input("Dolžini katet: ")
kateti = vnos.split(" ")
kateti[0] = int(kateti[0])
kateti[1] = int(kateti[1])
#hipotenuza = kateti[0] ** 2 + kateti[1] ** 2
#print (math.sqrt(hipotenuza))

def pitagora(a, b):
    hipotenuza1 = a ** 2 + b ** 2
    odgovor = math.sqrt(hipotenuza1)
    return odgovor


vrne = pitagora(kateti[0], kateti[1]) #to pisemo zato da dobimo input in pokličemo funkcijo da nam vrne hipotenuzo
print(vrne)