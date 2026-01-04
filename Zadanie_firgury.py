class FiguraGeometryczna:
    def policz_pole(self):
        pass

class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def policz_pole(self):
        return self.a * self.b

class Kwadrat(FiguraGeometryczna):
    def __init__(self, a):
        self.a = a
    def policz_pole(self):
        return self.a ** 2

prostokat = Prostokat(2,3)
kwadrat = Kwadrat(a=4)
print("Pole prostokata wynosi:", prostokat.policz_pole())
print("Pole kwadratu wynosi:", kwadrat.policz_pole())