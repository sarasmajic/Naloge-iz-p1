def nepadajoc(s):
    for i in range(len(s) - 1): #0123
        #print(i)
        #print(s[i])
        
        if s[i] < s[i + 1] or s[i] == s[i + 1]:
            continue
        
        else:
            return False
    
    return True
        
        





vrne = nepadajoc([1, 2, 3, 4, 5])
print(vrne)