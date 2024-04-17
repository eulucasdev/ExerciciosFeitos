n = int(input("Digite um número inteiro: "))
p = 0
for c in range(1, n+1):
    if n % c == 0:
        print("\33[1:33m", end="")
        print(c, end="\33[m:")
        p += 1
print(f"\nO número {n} foi divisível pelos {p} números a cima.")
if p == 2:
    print("\33[1:32mPor isso é um número primo\33[m")
else:
    print("\33[1:31mPor isso não é um número primo\33[m")
