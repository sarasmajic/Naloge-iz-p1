#Napiši funkcijo v_stavke(s), 
# ki kot argument dobi seznam nizov, ki predstavlja neko besedilo, 
# razbito po vrsticah (recimo tako, kot bi ga dobili iz datoteke, 
# če bi jo prebrali z readlines(), le brez znakov \n.) Kot rezultat 
# naj vrne taisto besedilo v seznamu, katerega elementi predstavljajo
#  stavke. Predpostavi, da se stavki vedno končajo s piko, klicajem 
# ali vprašajem ter da vse pike, klicaji in vprašaji pomenijo konec 
# stavka. Če tega ne znaš, pozabi na klicaje in vprašaje ter išči le 
# pike, vendar boš dobil(a) za to le polovico točk.

def v_stavke(s):
    str_s = "".join(s)
   

    for i in range(len(str_s)):
        if str_s[i] == ".":
            iskan_stavek = str_s[:i]
    print(iskan_stavek)
        #print(str_s) -- vrne mi crke
       


vrne = v_stavke(["Napiši funkcijo povedi, ki kot argument ", "sprejme nekaj. Kot rezultat ", "vrne nekaj drugega, ", "namreč seznam. ", "Kaj naj ta vsebuje? Eh, ",
"kaj neki, nize! Same ", "nize. ", "Da, tako bodi."])
print(vrne)