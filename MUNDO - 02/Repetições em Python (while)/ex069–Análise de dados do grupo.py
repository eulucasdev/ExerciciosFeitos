t18 = th = m20 = 0
while True:
    sexo = sn = " "
    idade = int(input("Idade? "))
    while sexo not in "fm":
        sexo = str(input("Sexo [F/M] ")).strip().lower()[0]
    while sn not in "sn":
        sn = input("Cadastrar outra pessoas? ")
    if idade >= 18:
        t18 += 1
    if sexo == "m":
        th += 1
    if sexo == "f" and idade < 20:
        m20 += 1
    if sn == "n":
        break
print(f"Total de homens: {th}\n"
      f"Total de pessoas maiores de 18: {t18}\n"
      f"Total de Mulheres maiores de 20 anos: {m20}")
