def leiadinheiro(v):
    while True:
        d = v.replace(",", "").replace(".", "").strip()
        c1 = v.count(",")
        c2 = v.count(".")
        c = c1 + c2
        if d.isnumeric() and c < 2:
            v = v.replace(",", ".")
            v = float(v)
            break
        else:
            print("\033[0:31mValor INCORRETO\033[m")
            v = input("Digite o valor: R$ ")
    return v





