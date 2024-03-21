n1 = int(input("Entre com primeiro número: "))
n2 = int(input("Entre com segundo número: "))
n3 = int(input("Entre com terceiro número: "))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"O Maior número é \033[1:34m{maior}\033[m e o menor número é \033[1:31m{menor}\033[m")

