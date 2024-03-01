from random import choice

print("-="*15)
print(f"{"SORTEIO":^30}")
print("=-"*15)
n1 = input("Primeiro nome: ")
n2 = input("Segundo nome: ")
n3 = input("Terceiro nome: ")
n4 = input("Quarto nome: ")
sor = [n1, n2, n3, n4]
esc = choice(sor)
print("#"*20)
print(f"{"RESULTADO":^20}")
print("#"*20)
print(f"O sorteado é: {esc.upper()}")

