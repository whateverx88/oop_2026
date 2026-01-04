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

class Kwadrat(FiguraGeometryczna):
    def __init__(self, a):
        self.a = a
    def policz_pole(self):
        return self.a ** 2
    def policz_obwod(self):
        return self.a * 4

prostokat = Prostokat(3,3)
kwadrat = Kwadrat(a=5)

print("Pole prostokata wynosi:", prostokat.policz_pole())
print("Obwod prostokata wynosi:", prostokat.policz_obwod())
print("Pole kwadratu wynosi:", kwadrat.policz_pole())
print("Obwod kwadratu wynosi:", kwadrat.policz_obwod())