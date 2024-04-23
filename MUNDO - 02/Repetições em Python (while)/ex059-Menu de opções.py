n1 = int(input("Entre com primeiro valor: "))
n2 = int(input("Entre com segundo valor: "))
maior = 0
sair = False
while not sair:
    op = int(
        input(
            "O que desejar fazer?\n"
            "[1] - SOMAR       [2] - SUBTRAIR\n"
            "[3] - MUTIPLICAR  [4] - DIVIDIR\n"
            "[5] - MAIOR       [6] - NOVOS NÚMEROS\n"
            "           [0] - SAIR\n"
        )
    )
    if op == 1:
        print(f"{n1} + {n2} = {n1+n2:.1f}")
    if op == 2:
        print(f"{n1} - {n2} = {n1-n2:.1f}")
    if op == 3:
        print(f"{n1} x {n2} = {n1*n2:.1f}")
    if op == 4:
        print(f"{n1} / {n2} = {n1/n2:.1f}")
    if op == 5:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O número maior é {maior}")
    if op == 6:
        n1 = int(input("Escolha um novo 1° valor: "))
        n2 = int(input("Escolha um novo 2° valor: "))
    if op == 0:
        sair = True
