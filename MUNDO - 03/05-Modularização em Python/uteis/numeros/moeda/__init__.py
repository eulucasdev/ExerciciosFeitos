# ----->  ex107 + ex111  <-----
def aumentar(valor=0, taxa=0, formata=False):
    res = valor + (valor * taxa/100)
    return res if not formata else real(res)


def diminuir(valor=0, taxa=0, formata=False):
    res = valor - (valor * taxa/100)
    return res if not formata else real(res)


def dobro(valor=0, formata=False):
    res = valor * 2
    return res if not formata else real(res)


def metade(valor=0, formata=False):
    res = valor / 2
    return res if not formata else real(res)


# ----->  ex108  <-----
def real(valor=0, moeda="R$"):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')


def resumo(v, up=0, dow=0):
    print("="*35)
    print(f"{"RESUMO DE VALOR":^35}")
    print("="*35)
    print(f"Preço analisado: \t{real(v)}")
    print(f"Dobro do preço: \t{dobro(v, True)}")
    print(f"Metade do preço: \t{metade(v, True)}")
    if up < 10:
        print(f"0{up}% de aumento: \t{aumentar(v, up, True)}")
    else:
        print(f"{up}% de aumento: \t{aumentar(v, up, True)}")
    if dow < 10:
        print(f"0{dow}% de redução: \t{diminuir(v, dow, True)}")
    else:
        print(f"{dow}% de redução: \t{diminuir(v, dow, True)}")
    print("="*35)
