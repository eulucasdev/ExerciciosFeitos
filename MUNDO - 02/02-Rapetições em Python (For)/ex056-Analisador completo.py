anos = mm20 = ihmv = 0
nhmv = ""
for c in range(1, 5):
    nome = input("NOME: ")
    idade = int(input("IDADE: "))
    sexo = input("GÊNERO [M/F]:").lower().strip()[0]
    anos += idade
    if sexo == "m" and idade > ihmv:
        ihmv = idade
        nhmv = nome
    if sexo == "f" and idade < 20:
        mm20 += 1
print("-="*15)
print(f"A idade média do grupo é de: {anos/4:.1f}"
      f"\nO homen mais velho se chama: {nhmv}"
      f"\nE o total de mulheres menores de 20 anos são: {mm20}")
