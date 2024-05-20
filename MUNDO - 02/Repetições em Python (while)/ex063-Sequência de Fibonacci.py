print("."*30)
print(f"{"Sequência de Fibonacci":^30}")
print("°"*30)
t = int(input("Quantos termos quer ver? "))
t1 = 0
t2 = 1
print("-="*15)
print(f"{t1} -> {t2}", end="")
c = 3
while c <= t:
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2
    t2 = t3
    c += 1
print(" -> FIM!")
