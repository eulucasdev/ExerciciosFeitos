print("₢"*25)
print(f"{"TRIÂNGULOS":^25}")
print("₢"*25)
r1 = float(input("Medida da 1° reta: "))
r2 = float(input("Medida da 2° reta: "))
r3 = float(input("Medida da 3° reta: "))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    r = "\033[1:33mSIM\033[m"
else:
    r = "\033[1:31mNÃO\033[m"
print("-*-"*12)
print(f"{r} é possivel fazer um triângulo!")
