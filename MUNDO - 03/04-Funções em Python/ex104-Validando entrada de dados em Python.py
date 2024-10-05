def leiaInt(nu):
    while True:
        n = str(input(nu))
        if not n.isnumeric():
            print("\033[0:31mErro! Digite um número inteiro válido.\033[m")
        elif n.isnumeric():
            break
    return n


n = leiaInt("Digite um número: ")
print(f"\033[0:32mNúmero {n} registrado!\033[m")
