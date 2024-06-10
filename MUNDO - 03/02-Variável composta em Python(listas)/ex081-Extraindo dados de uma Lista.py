num = list()
while True:
    num.append(int(input("Digite um número: ")))
    res = input("Deseja continuar? [S/N]").strip().lower()[0]
    while res not in "sn":
        res = input("ERRO! DIGITE S ou N]").strip().lower()[0]
    if res == "n":
        break
print("*."*15)
print(f"\nForam digitados {len(num)} números.")
num.sort(reverse=True)
print(f"\n Números digitados em ondem decrescente{num}")
if 5 in num:
    print(f"\nO número 5 foi digitado {num.count(5)} vezes ")
else:
    print("\nO valor 5 não foi encontrado.")
