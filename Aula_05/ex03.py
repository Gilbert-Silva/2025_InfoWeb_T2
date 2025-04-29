class Triangulo():
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2  

# x é a Referência  Triangulo() é a instância ou objeto
x = Triangulo()
x.b = 10
x.h = 20

y = Triangulo()
y.b = 30
y.h = 40

z = x
z.b = 50
z.h = 100

print(x.b, x.h)
print(id(x))
print(id(y))
print(id(z))


a = 5
b = 5
print(id(a))
print(id(b))

