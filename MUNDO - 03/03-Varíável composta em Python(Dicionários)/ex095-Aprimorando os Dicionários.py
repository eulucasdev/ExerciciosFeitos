grupo = list()
while True:
    jogador = dict()
    gols = list()
    jogador['nome'] = str(input("Nome do jogador: "))
    parti = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for p in range(1, parti+1):
        gol = int(input(f"Quantos gols na {p}° partida: "))
        gols.append(gol)
    jogador['gols'] = gols.copy()
    grupo.append(jogador)
    print("-="*15)
    while True:
        res = str(input("Cadastrar outro jogador [S/N]")).strip().upper()[0]
        if res in "SN":
            break
        print("ERRO! RESPONDA S OU N")
    if res == "N":
        break
print("=-"*15)
print(f"{'COD':<5}{'NOME':<15}{'GOLS':<18}{'TOTAL':<22}")
print("-_"*25)
for k, v in enumerate(grupo):
    print(f"{k:<5}{v['nome'].title():<15}{f"{v['gols']}":<18}{sum(v['gols']):<23}")
print("_-"*25)
while True:
    print("[999 PARA ENCERRAR]")
    das = int(input("CÓDIGO JOGADOR: "))
    if das <= len(grupo)-1:
        print(f" - - Informações de {grupo[das]['nome'].title()} - - ")
        for v in range(0, len(grupo[das]['gols'])):
            print(f'Na {v+1}° partida fez {grupo[das]['gols'][v]} gols.')
    elif das == 999:
        break
    elif das > len(grupo)-1:
        print("ERRO! Não há jogador com esse código!")
    print("=="*15)
print("PROGRAMA FINALIZADO")
