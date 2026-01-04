# Program do zarzadzania mala firma
from encodings.punycode import selective_find

# Bez programowania obiektowego:

#pracownik1_imie = "Adam"
#pracownik1_nazwisko = "Nowak"
#pracownik1_pensja = "4500"

#pracownik2_imie = "Anna"
#pracownik2_nazwisko = "Nowak"
#pracownik2_pensja = "4500"

#pracownik2_pensja = pracownik2_pensja + 100

# Programowanie Obiektowe OOP

class Pracownik:
        def __init__(self, imie, nazwisko, pensja):
            self.imie = imie
            self.nazwisko = nazwisko
            self.pensja = pensja
            print(f"Dane pracownika:"
                  f"\nImie: {self.imie} "
                  f"\nNazwisko: {self.nazwisko} "
                  f"\nPensja: {self.pensja}")

adam_nowak = Pracownik("Adam", "Nowak", "4500")

print(adam_nowak)
