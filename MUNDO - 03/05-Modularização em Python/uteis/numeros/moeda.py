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
