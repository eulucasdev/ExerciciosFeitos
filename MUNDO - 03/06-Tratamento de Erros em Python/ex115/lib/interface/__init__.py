def titulo(msg):
    print("-"*30)
    print(msg.center(30))
    print("-"*30)


def menu(lista):
    titulo("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
    print("-"*30)
