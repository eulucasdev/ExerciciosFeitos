matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = sc = msl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor para [{l}][{c}]: "))
print("*"*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            sc += matriz[l][c]
        if matriz[1][c] > msl:
            msl = matriz[1][c]
    print()
print("-="*15)
print(f"Soma de todos os pares: {sp}")
print(f"Soma da 3° coluna: {sc} ")
print(f"Maior valor da 2° linha: {msl}")
