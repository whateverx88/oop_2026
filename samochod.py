class Pojazd:
    def jedz(self):
        print(f"Jade samochodem marki {self.marka} {self.model}...")
    def hamuj(self):
        print("Hamuje...")

class Samochod(Pojazd):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Honda(Samochod):
    def __init__(self, model):
        super().__init__("Honda", model)

audi = Samochod("Audi", "A4")
audi.jedz()
honda = Honda("Civic")
honda.jedz()