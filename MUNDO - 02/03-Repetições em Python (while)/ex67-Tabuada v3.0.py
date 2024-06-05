while True:
    n = int(input("Ver a tabúada de qual valor? "))
    if n < 0:
        break
    print("-="*15)
    for c in range(1, 11):
        print(f"{c:>2} x {n:^2}  = {n*c:>3}")
    print("=-"*15)
print("Fim do Programa!")
