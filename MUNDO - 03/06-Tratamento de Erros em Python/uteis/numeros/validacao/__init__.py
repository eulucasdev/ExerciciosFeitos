def leiaInt(nu=0):
    while True:
        try:
            n = int(input(nu))
        except (ValueError, TypeError):
            print("\033[0:31mErro! Digite um número inteiro válido.\033[m")
        except (KeyboardInterrupt):
            print("\033[0;33mO Usuario preferiu não informar!\033[m")
            return 0
        else:
            break
    return n


def leiaReal(r=0):
    while True:
        try:
            r = float(input(r))
        except (ValueError, TypeError):
            print("\033[0:31mERRO! Digite um número real válido.\033[m")
        except (KeyboardInterrupt):
            print("\033[0:33mO usuario preferio não infromar\033[m")
            return 0
        else:
            break
    return r
