def leiadinheiro(v):
    while True:
        d = v.replace(".", "")
        d = d.replace(",", "")
        c1 = v.count(",")
        c2 = v.count(".")
        c = c1 + c2
        if d.isnumeric() and c == 1:
            v = v.replace(",", ".")
            v = float(v)
            break
        else:
            print("Valor INCORRETO")
            v = input("Digite o valor: R$ ")
    return v
