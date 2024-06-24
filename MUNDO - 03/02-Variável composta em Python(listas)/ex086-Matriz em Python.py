matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Qual valor na posição [{l}], [{c}]: "))
print("-="*15)
for m in range(0, 3):
    for p in range(0,3):
        print(f"[{matriz[m][p]:^5}]", end='')
    print()

