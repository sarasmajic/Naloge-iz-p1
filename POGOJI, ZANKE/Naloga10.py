vnos = input("Vnesi število: ")
st = int(vnos)
print(st)

while st != 1: #ta st del to je pogoj, naj se loop izvaja dokler ni enako 1, ker enkrat ko bo ena naj gre vn iz loopa
    if st % 2  == 0: #ce je stevilo sodo
        st = st // 2
    
    else: #za liha st
        st = st * 3 + 1
    

    print(st)




