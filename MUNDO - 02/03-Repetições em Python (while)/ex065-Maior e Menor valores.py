s = "s"
maior = menor = soma = c = n = 0
while s in "s":
    n = int(input("Digite un número: "))
    soma += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    s = str(input("QUER CONTINUAR? [S/N]")).lower().strip()[0]
print(f"Foi digitado {c} valores.\nA média de todos os números digitados é {soma/c}.\n"
      f"O Maior número digitado é: {maior}\n"
      f"O Menor número digitado é: {menor}")
