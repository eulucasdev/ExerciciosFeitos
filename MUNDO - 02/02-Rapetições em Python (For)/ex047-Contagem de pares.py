n = int(input("quer ver os pares até qual número: "))
quebra = 0
for c in range(1, n+1):
    if c >= quebra or c == 50:
        print("\n")
        quebra += 50
    if c % 2 == 0:
        print(c, end=" ")
print("FIM!!!")

