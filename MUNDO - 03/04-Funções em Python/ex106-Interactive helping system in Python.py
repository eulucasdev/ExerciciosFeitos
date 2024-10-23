from time import sleep
def title(msg):
    tam = len(msg) + 4
    print("~"*tam)
    print(f"{msg:^{tam}}")
    print("~"*tam)


def ajuda():
    while True:
        print("\033[01;30;42m", end="")
        title('SISTEMA DE AJUDA PyHELP')
        msg = input("\033[mQual comando quer saber?").lower().strip()
        print("\033[01;31;44m", end="")
        if msg != "fim":
            title(f"Acessando o manual do comando '{msg}' ")
            print("\033[m", end="")
            sleep(2)
            print("\033[1;30;47m")
            help(msg)
        if msg == "fim":
            break
    print("\033[m\033[01;31;43mPROGRAMA ENCERRADO!")


ajuda()
