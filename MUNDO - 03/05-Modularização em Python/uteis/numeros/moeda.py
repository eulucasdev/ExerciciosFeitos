# ----->  ex107  <-----
def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res


# ----->  ex108  <-----
def real(valor):
    res = f"R$ {valor:.0f},00"
    return res
