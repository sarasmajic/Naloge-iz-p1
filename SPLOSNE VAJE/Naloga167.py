def kako_visoko(s):
    for i in range(len(s) - 1):
        razlika = s[i + 1] - s[i]
        #print(razlika)
        #print(s[i + 1])
        #print(s[0]) vrne 30, s[i] --> vrne vse cifre
        
        if s[0] > 20:
            print(0)
            break
        
        if razlika > 20:
                print(s[i])
                
        elif razlika <= 20:
            print(s[-1])



vrne = kako_visoko([10, 20, 25, 45, 50, 71, 98, 110])
print(vrne)