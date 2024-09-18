def fator(f, show=False):
    """
fator(n, show=False)
    -> Calcula o Fatorial de um número
    :param f: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    print(f, end=" x ")
    for c in range(f-1, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(c, end=" x ")
            else:
                print(c, end=" = ")
    return f


print(fator(5, show=True))
