c = 0
while True:
    n = int(input("Ver a tabúada de qual valor? "))
    print("-="*15)
    if n < 0 :
        break
    elif c == 10:
        c = 0
    while c != 10:
        c += 1
        print(f"{n:>5} x {c:>2} = {n*c:>2}")
    print("=-"*15)
print("Fim do Programa!")
