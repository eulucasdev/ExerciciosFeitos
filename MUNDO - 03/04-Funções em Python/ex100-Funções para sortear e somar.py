from random import randint
from time import sleep

sorteados = list()


def sorteia():
    for c in range(0, 5):
        num = randint(1, 100)
        sorteados.append(num)
    print(f"Os números sorteados são: ", end="")
    for c in sorteados:
        print(c, end=", ")
        sleep(0.5)
    print()


def somapar():
    s = cont = 0
    print(f"A soma entre os números pares sorteados")
    for n in sorteados:
        if n % 2 == 0:
            print(n, end=" ")
            s += n
    print(f" = {s}")


sorteia()
somapar()
