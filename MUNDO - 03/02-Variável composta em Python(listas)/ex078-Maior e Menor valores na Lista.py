numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input("Insira um numero: ")))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print("=-"*15)
print(f"Você digitou os números: {numeros}")
print(f"O maior número da lista é {maior} e se encontra nas posições: ", end="")
for po, nu in enumerate(numeros):
    if nu == maior:
        print(po, end="...")
print(f"\nO menor número da lista é {menor} e se encontra nas posições: ", end="")
for po, nu in enumerate(numeros):
    if nu == menor:
        print(po, end="...")
