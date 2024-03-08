num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"UNIDADE: {u}\n"
      f"DEZENA: {d}\n"
      f"CENTENA: {c}\n"
      f"MILHAR: {m}")

