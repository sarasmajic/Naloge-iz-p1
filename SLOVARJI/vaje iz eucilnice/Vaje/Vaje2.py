#najvisje temp, izmerjene na vsaki postajio

najvisje = {}

for vrstica in open("vremenske-postaje.txt"):
    kraj, datum, najvisja, najnizja = vrstica.split(",")
    najvisja = int(najvisja)
    najnizja = int(najnizja)

    #print(najvisja)

    if kraj not in najvisje or najvisje[kraj] < najvisja: #ce kraja ni v slovarju kar ga ni, dodajo se kraji in prva najvisja temp. zapisana zato vedno vrne -1, -6 itd..
       #dodamo ce je ta prva temperatura manjsa od najvisje kar je enkrat ko pridemo do najvisje se konča in se zapiše
        najvisje[kraj] = najvisja  #value najvisja_temp od dolocenega kraja naj se nastavi na to najvisjo videno vrednost

for kraj, najvisja in najvisje.items():  #vrača par ključ-vrednost (crnomelj 40, maribor 40)
    print(kraj, najvisja)