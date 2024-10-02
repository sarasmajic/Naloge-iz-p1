def sama_liha(s):
    st_lihih = 0

    for e in s:
        if e % 2 != 0:
            st_lihih += 1
        
    
    if st_lihih == len(s) or len(s) == 0:
        return True
    else:
        return False

vrne = sama_liha([1, 3, 7])
print(vrne)
