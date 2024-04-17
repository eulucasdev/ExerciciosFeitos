print("TERMOS DE UMA P.A")
print("=-"*15)
t = int(input("Qual é o termo: "))
r = int(input("Qual a razão: "))
q = int(input("Quantos temos que mostrar:"))
print("-="*15)
q = t + (q - 1) * r
cont = 15
co = 0
for c in range(t, q+r, r):
    print(c, end=" > ")
    co += 1
    if co > cont:
        print("\n")
        cont += 15
print("FIM!")
