#Klasa szablon przepis
import random

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
        print (f"Niech powstanie Czlowiek o imieniu {imie} oraz plci {plec}")
        self.imie = imie
        self.plec = plec
        #adam.imie = "Adam"
        #ewa.imie = "Ewa"

    def __add__(self, other):
        if isinstance(other, Czlowiek) and self.plec != other.plec:
            return Dziecko(None, random.choice("MK"))

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
    def __init__(self, imie, plec):
        print(f"Rodzi sie Dziecko o imieniu {imie} oraz plci {plec}")
        super().__init__(imie, plec)

    def __str__(self):
        return f"Dziecko {self.imie} {self.plec}"

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
#mariola = Czlowiek("Mariolka", "K")
#kain = Dziecko("Kain", "M")
dziecko = adam + ewa
#print(type(adam))
#print(dir(adam))
#print(dir(Czlowiek))
#print(adam.gatunek)
#print(ewa.gatunek)
#print(ewa.imie)
#print(adam.imie)
#ewa.przedstaw_sie()
#ewa.przedstaw(kain)
#kain.przedstaw_sie()
#kain.przedstaw(adam)
#kain.baw_sie()
#print(dir(Czlowiek))
#print(dir(adam))
#print(dir(kain))
#print(Czlowiek)
#print(kain)
#print(str(kain))
#print(kain.__str__())
#print(adam)
#print(ewa)

#abel = Dziecko("Abel", "M")
#print(abel.plec)
#print(dziecko)
