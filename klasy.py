#Klasa szablon przepis
class Czlowiek:
    #Istota
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
    #Konstruktor
    #Akt istnienia
        print (f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie

#powstanie oboektu, gotowanie z przepisu
adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
#print(type(adam))
#print(dir(adam))
#print(dir(Czlowiek))
print(adam.gatunek)
print(ewa.gatunek)
print(ewa.imie)
print(adam.imie)