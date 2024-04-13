print("TERMOS DE UMA P.A")
print("=-"*10)
t = int(input("Qual é o termo: "))
r = int(input("Qual a razão: "))
q = int(input("Quantos temos que mostrar:"))
cont = 15
for c in range(1, q+1):
    if c > cont:
        print("\n")
        cont += 15
    if c <= q:
        print(t, end=" > ")
        t += r
print("FIM!")
