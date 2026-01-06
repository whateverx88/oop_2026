from string import digits


class FiguraGeometryczna:
    def policz_pole(self):
        pass
    def policz_obwod(self):
        pass

class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def policz_pole(self):
        return self.a * self.b
    def policz_obwod(self):
        return 2 * self.a + 2 * self.b

#class Kwadrat(FiguraGeometryczna):
#    def __init__(self, a):
#        self.a = a
#    def policz_pole(self):
#        return self.a ** 2
#    def policz_obwod(self):
#        return self.a * 4

class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)
        #Prostokat(a, a)

class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r
    def policz_pole(self):
        return 3.14 * self.r ** 2
    def policz_obwod(self):
        return 2 * 3.14 * self.r

prostokat = Prostokat(3,3)
kwadrat = Kwadrat(3)
kolo = Kolo(6)

print("Pole prostokata wynosi:", prostokat.policz_pole())
print("Obwod prostokata wynosi:", prostokat.policz_obwod())
print("Pole kwadratu wynosi:", kwadrat.policz_pole())
print("Obwod kwadratu wynosi:", kwadrat.policz_obwod())
print("Pole kola wynosi:", kolo.policz_pole())
print("Obwod kola wynosi", kolo.policz_obwod())