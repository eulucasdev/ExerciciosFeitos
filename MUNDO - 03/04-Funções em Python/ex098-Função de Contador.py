from time import sleep


def contador(i, f, p):
    print("-=" * 15)
    if p < 0:
        p *= -1
    print(f"Contando de {i} até {f} de {p} em {p}")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="")
            sleep(0.3)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="")
            sleep(0.3)
            cont -= p
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("=-"*15)
print("Sua vez de contar!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
while True:
    pas = int(input("Passo: "))
    if pas == 0:
        print("O PASSO NÃO PODE SER 0(ZERO)")
    else:
        break
contador(ini, fim, pas)
