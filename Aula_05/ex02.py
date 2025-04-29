class Triangulo():
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2    

x = Triangulo()
y = Triangulo()

s = "InfoWeb"
s = str()

print(x, type(x))
x.b = 10
x.h = 20
print(x.b, x.h)
#print(x.b * x.h / 2)
print(x.calc_area())

print(y, type(y))
y.b = 30
y.h = 40
print(y.b, y.h)
#print(y.b * y.h / 2)
print(y.calc_area())


l = []
l = list()
print(type(l))
l.append(10)

#class list:
#    def __init__(self):
#        pass
#    def append(valor):
#        pass
