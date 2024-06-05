from random import randint
v = 0
while True:
    pc = randint(0, 10)
    p1 = int(input("Escolha um número inteiro de 1 a 10: "))
    soma = pc+p1
    esc = " "
    while esc not in "pi":
        esc = str(input("você que impar ou par? ")).strip().lower()[0]
    print("-="*10)
    print(f"Você escolheu {p1} e eu escolhi {pc}.")
    if esc in "i":
        if soma % 2 == 0:
            print(f"{soma} é par, EU GANHEI!")
            break
        else:
            print(f"{soma} é impar, VOCÊ GANHOU!")
            v += 1
    else:
        if soma % 2 == 0:
            print(f"{soma} é par, VOCÊ GANHOU!")
            v += 1
        else:
            print(f"{soma} é impar, EU GANHEI!")
            break
    print("=-"*10)
    print("Vamos jogar novamente.")
print(f"Você teve {v} vitórias.")