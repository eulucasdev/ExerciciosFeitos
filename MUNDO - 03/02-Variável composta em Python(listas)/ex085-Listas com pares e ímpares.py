numeros = [[], []]
print("*"*40)
print(F"{'ESSE NÚMERO É PAR OU IMPAR?':^40}")
print("*"*40)
for num in range(0, 7):
    n = int(input("Entre com um número: "))
    if n % 2 == 0:
        numeros[0].append(n)
    if n % 2 != 0:
        numeros[1].append(n)
print("-="*15)
numeros[0].sort()
numeros[1].sort()
print(f"Os valores pares são: {numeros[0]}")
print(f"Os impares são: {numeros[1]}")
