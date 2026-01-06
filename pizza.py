# Korzystając ze stworzonych uprzednio  figur geometrycznych, stwórz klasę Pizza.

# Ma ona bazować na Kole oraz posiadać:
# cenę
# metodę liczącą opłacalność
# Pizza posiada listę składników
# Pizza jest w stanie sprawdzić, czy w składnikach znajduje się alergen
# USER STORIES:
# Jako konsument pizzy chciałbym, żeby aplikacja była w stanie policzyć opłacalność pizzy, żeby móc
# porównywać pizze ze sobą.

# Jako konsument pizzy, chciałbym wiedzieć, czy pizza zawiera alergen na który jestem uczulony.

from Zadanie_firgury import Kolo

class Pizza(Kolo):
    def __init__(self, d, cena, *args):
        self.ciasto = ciasto
        self.sos = sos
        self.skladniki = skladniki

    def policz_oplacalnosc
