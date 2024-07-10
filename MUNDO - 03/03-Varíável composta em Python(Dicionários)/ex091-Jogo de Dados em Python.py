from random import randint
jogos = dict()
for c in range(1, 5):
    dados = {input("nome:"): randint(1, 6)}
    jogos.update(dados)
print(f"Os valores sorteados foram:")
for k, v in jogos.items():
    print(f"O {k:<8} tirou {v}")
print("-="*15)
for i in sorted(jogos, key=jogos.get, reverse=True):
    print(f"1° Lugar {i:<8} com: {jogos[i]:}")
