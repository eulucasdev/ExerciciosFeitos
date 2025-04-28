def leiaReal(r):
    while True:
        try:
            r = float(input(r))
        except (ValueError, TypeError):
            print("\033[0:31mERRO! Digite um número real válido.\033[m")
        except (KeyboardInterrupt):
            print("\033[0:33mO Usuario preferio não infromar\033[m")
            return 0
        else:
            break
    return r


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO")
            continue
        except (KeyboardInterrupt):
            print("USUÁRIO PREFERIU NÃO DIGITAR")
            return 0
        else:
            return n
