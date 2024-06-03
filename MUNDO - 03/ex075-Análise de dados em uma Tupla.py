n = (int(input("Digite um número: ")), int(input("Digite um número: ")),
     int(input("Digite um número: ")), int(input("Digite um número: ")), )
print(f"O número 9 apareceu: {n.count(9)} vezes.")
if not 3 in n:
    print("O valor 3 não aparece nenhuma vez.")
else:
    print(f"O valor 3 aparece primeiro na posição: {n.index(3)+1}")
print("Os valores pares digitados são: ", end="")
for c in n:
    if c % 2 == 0:
        print(c,   end=" ")
