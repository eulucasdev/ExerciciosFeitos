def ficha(n, g):
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if not n.isalpha():
        n = "{DESCONHECIDO}"
    print(f"O jogador {n} fez {g} gol(s)")


ficha(n=str(input("Nome do jogador: ")).strip(), g=str(input("Número de gols: ")).strip())
