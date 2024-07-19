grupo = list()
f = list()
si = 0
while True:
    pessoa = dict()
    pessoa["nome"] = input("Nome: ").title()
    while True:
        pessoa["sexo"] = input("Sexo [M/F]: ").strip().upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Digite apenas M ou F")
    if pessoa["sexo"] == "F":
        f.append(pessoa)
    pessoa["idade"] = int(input("Idade: "))
    si += pessoa["idade"]
    grupo.append(pessoa)
    while True:
        r = input("Cadastrar outra pessoa? ").strip().lower()[0]
        if r in "sn":
            break
        print("ERRO! Responda S ou N apenas!")
    print("=" * 30)
    if r == "n":
        break
print(f"- Foram cadastradas {len(grupo)} pessoas.")
print(f"- A idade média do grupo é de: {si/len(grupo):5.2f} anos.")
print("- As mulheres do grupo são:")
for n in f:
    print(f"{n['nome'].title()}", end=" - ")
print("\n- Pessoas com idade acima da média: ")
for p in grupo:
    if p["idade"] > si/len(grupo):
        print("    ", end="")
        for k, v in p.items():
            print(f"{k.upper()}: {v} - ", end="")
        print()
print("-=" * 15)
print("\n  << FIM DO PROGRAMA >>")
