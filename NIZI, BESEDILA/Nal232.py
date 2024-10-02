def sifrirano(bes):  #neki ne dela ok
    stavek = bes.split(".")
    string = ""
    #print(stavek)
    for i,st in enumerate(stavek):
 
        st = st.split(" ") #st je seznam z vsemi besedami
        for el in st:
            if el != " " and el.isupper() == True:
                string += el
            else:
                pass
        #print(st)
        #print(st[])
    print(string)
        

vrne = sifrirano("Nic ne bo. Ana bo ostala doma. Prisla je njena mama. Aleksa tudi ne bo. Dejan je zbolel. Groza. Ostali smo samo se jaz, ti in Miha. Bolje, da izlet prestavimo. Pa tako sem se ga veselil. 6 dni sem cakal na to, da se odpravimo v hribe. Hja, pa drugic...")
print(vrne)