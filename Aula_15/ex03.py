x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
y = x.copy()

print(id(x))
print(id(y))

x["SP"] = "São Paulo"
print(y)
