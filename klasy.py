#Klasa szablon przepis
class Czlowiek:
    #Istota
    #aAtrybuty klasy
    # cechy wspolne kazdego czlowieka
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec): #atrbuty OBIEKTU (skladniki potrawy)
    #Cechy konkretnej osoby
    #Konstruktor
    #Akt istnienia
    #Gotowanie
        print (f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec
        #adam.imie = "Adam"
        #ewa.imie = "Ewa"

    #metoda
    #moznosc, mozliwosc, zdolnosc
    def przedstaw_sie(self):
        print(f"Dzien dobry. Mam na imie {self.imie} i jestem ", end="")
        if self.plec=="M":
            print("mezczyzna")
        else:
            print("kobieta")
    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}. {osoba.imie} jest ", end="")
        if osoba.plec=="M":
            print("mezczyzna")
        else:
            print("kobieta")

class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Ale zabawa, juhuuu!!!")
    def przedstaw_sie(self):
        print(f"Cesc, jestem {self.imie}. jestem ", end="")
        if self.plec=="M":
            print("chlopcem")
        else:
            print("dziewczynka")

#powstanie obiektu, gotowanie z przepisu
adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")
mariola = Czlowiek("Mariolka", "K")
kain = Dziecko("Kain", "M")
#print(type(adam))
#print(dir(adam))
#print(dir(Czlowiek))
print(adam.gatunek)
print(ewa.gatunek)
print(ewa.imie)
print(adam.imie)
ewa.przedstaw_sie()
ewa.przedstaw(mariola)
kain.przedstaw_sie()
kain.baw_sie()