p = s = c = 0
p = int(input("Entre com um número inteiro: "))
while p != 999:
    print("Digite 999 para encerrar!")
    c += 1
    s += p
    p = int(input("Entre com um número inteiro: "))
print(f"Foi registrado {c} entradas.\nA soma delas deu: {s}")
