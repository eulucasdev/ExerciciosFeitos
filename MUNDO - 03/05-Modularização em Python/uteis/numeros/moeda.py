# ----->  ex107  <-----
def aumentar(valor=0, taxa=0):
    res = valor + (valor * taxa/100)
    return res


def diminuir(valor=0, taxa=0):
    res = valor - (valor * taxa/100)
    return res


def dobro(valor=0):
    res = valor * 2
    return res


def metade(valor=0):
    res = valor / 2
    return res


# ----->  ex108  <-----
def real(valor=0, moeda="R$"):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')
