import random

def vrzi():
    return random.choice("GC")

k = 5 #stevilo kovancev ki jih ima Ben

while k != 10 and k > 0: #or ni ker se oba pogoja morata izpolnjevat
    if vrzi() == "G":
        k = k - 1
    
    else:
        k = k + 1
    
    print(k)


