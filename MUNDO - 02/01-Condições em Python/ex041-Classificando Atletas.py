from datetime import date
titulo = "Confederação Nacional de Natação"
print("~"*len(titulo))
print(titulo)
print("~"*len(titulo))
ano = date.today().year
nas = int(input("Qual ano de seu nascimento? "))
idade = ano - nas
if idade > 25:
    r = "MASTER"
elif idade > 19:
    r = "SÊNIOR"
elif idade > 14:
    r = "JÚNIOR"
elif idade > 9:
    r = "INFANTIL"
else:
    r = "MIRIM"
print(f"Você tem {idade} anos e pertence a categoria: {r}")
