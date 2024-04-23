s = input("Qual seu sexo [F/M]: ").lower().strip()[0]
r = ""
while s not in "fm":
    s = input("Dado invalido! INFORME [F OU M]: ").lower().strip()[0]
if s == "m":
    r = 'MASCULINO'
else:
    r = 'FEMININO'
print(f"Gênero {r} registrado.")
