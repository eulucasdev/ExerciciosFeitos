num = []
while True:
    val = int(input("Digite um valor: "))
    if val in num:
        print(f"Esse número já consta, informe outro!")
    else:
        num.append(val)
        print(f"Número {val} adicionado!")
    res = input("Continuar? [N/S]").strip().lower()[0]
    if res in "Nn":
        break
print("="*30)
print(f"os números digitados são: {sorted(num)}")
