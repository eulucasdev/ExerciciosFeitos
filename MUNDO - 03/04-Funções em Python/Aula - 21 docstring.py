def contador(i, f, p=1):
    """
    - Essa funça faz uma contagem e mostra na tela.
    - Quando o passo é = 0 ele se torna 1
    - Os parâmetros são informados pelo usuário

    :param i: Início da contagem
    :param f: Termino da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    if p == 0:
        p = 1
    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM!")


print(contador.__doc__)
help(contador)
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))
