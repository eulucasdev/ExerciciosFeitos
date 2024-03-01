from random import shuffle
print(f"{"SORTEIO":^30}")
print("=-"*15)
n1 = input("Primeiro nome: ")
n2 = input("Segundo nome: ")
n3 = input("Terceiro nome: ")
n4 = input("Quarto nome: ")
sor = [n1, n2, n3, n4]
shuffle(sor)
print("#"*30)
print(f"{"ORDEM DE APRESENTAÇÃO":^30}")
print("#"*30)
print(f"O sorteado é: {sor}")
