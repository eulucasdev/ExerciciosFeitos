jog = list()
while True:
    play = dict()
    print("-=" * 15)
    play["nome"] = input("\nJogador: ").strip().title()
    play["partidas"] = int(input(f"Quantas partidas {play['nome']} Jogou: "))
    gols = 0
    for v in range(1, play["partidas"] + 1):
        gol = int(input(f"Quantos gols na {v}° partida: "))
        gols += gol
    play["t.gols"] = gols
    print("=-" * 15)
    res = input("Registrar outro jogador? [S/N]: ").strip().upper()[0]
    jog.append(play)
    if res in "N":
        break
print("-="*15)
while True:
    a = 0
    busca = input("Buscar informação de qual jogador /[0] para sair: ").strip().title()
    if busca == "0":
        break
    elif busca != "0":
        for c in jog:
            if busca in c['nome']:
                for v, k in c.items():
                    print(f"{v}: {k}")
                    a += 1
