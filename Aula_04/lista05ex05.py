def formatar_nome(nome):
    nome = nome.lower()
    nome = nome.split()
    r = ""
    for palavra in nome:
        if palavra in ["da", "de", "do", "das", "dos", "e"]:
            r = r + palavra + " "
        else:                   
            r = r + (palavra[0].upper() + palavra[1:]) + " "
    return r

print("Digite seu nome:")
nome = input()
r = formatar_nome(nome)        
print(r)        
        


