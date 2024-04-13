soma = cont = 0
for c in range(1, 7):
    n = int(input(f"Digite o {c}° valor: "))
    if n % 2 == 0:
        soma += n
        cont += 1
print("- "*10)
print(f"Foi informado {cont} números pares\n"
      f"e a soma deles é: {soma}")