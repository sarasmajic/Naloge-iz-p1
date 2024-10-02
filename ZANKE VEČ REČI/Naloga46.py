def arg_max(s):
    max = -10000000
    max_index = -1
    for i in range(len(s)):
        if s[i] > max:
            max = s[i]
            max_index = i  #shranimo si max index da ga nerabimo potem iskat tko kokr sm ga jst iskala v naslednjem range loopu

    #for i in range(len(s)):
    #    if s[i] == max:
    #        return i
    
    #print(max)
        #print(i)
    return max_index


vrne = arg_max([5, 1, 4, 2, 20, 3])
print(vrne)