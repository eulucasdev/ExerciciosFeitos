# ----->  ex107 + ex109  <-----
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
    print(f"Preço analisado:{real(v):<18}")
    print(f"Dobro do preço:{dobro(v, True):<19}")
    print(f"Metade do preço:{metade(v, True):<18}")
    print(f"{up}% de aumento:{aumentar(v, up, True):<19}")
    print(f"{dow}% de redução:{diminuir(v, dow, True):<19}")
    print("="*35)

