x = [10, 5, 8, 4]
y = ["a", "C", "B", "0"]
print(max(x))
print(max(y)) # Lexicográfica
print(type(x))
x[0] = 3
#print(x[10])

x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
print(type(x))

print(x["RN"])
x["AM"] = "Manaus"
x["PB"] = "J. Pessoa"
x[1] = "Teste"
print(x)
#print(x["SP"])
