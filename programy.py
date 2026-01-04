class Zloty(float):
    def __add__(self, other):
        return Zloty(super().__add__(other))

    def zamien_na_euro(self):
        return self/4.21 #bo to bedzie float!

a = Zloty(4)
b = Zloty(7)

c = a + b

print(c)
print(type(a))
print(c.zamien_na_euro())
