#Klasa szablon przepis
class Czlowiek:
    #Istota
    gatunek = "Homo Sapiens"
    def __init__(self):
    #Konstruktor
    #Akt istnienia
        print ("Niech powstanie Czlowiek")


#powstanie oboektu, gotowanie z przepisu
adam = Czlowiek()
#print(type(adam))
#print(dir(adam))
#print(dir(Czlowiek))
print(adam.gatunek)