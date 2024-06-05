s = c = 0
while True:
    print("DIGITE 999 PARA SAIR")
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    s += n
    c += 1
print(f"{c} valores digitados.\n"
      f"A soma de todos eles é: {s}")
