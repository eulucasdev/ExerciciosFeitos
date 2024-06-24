lista_pes = list()
pes = list()
ma = me = 0
while True:
    pes.append(str(input("Nome: ")))
    pes.append(float(input("Peso: ")))
    if len(lista_pes) == 0:
        ma = me = pes[1]
    else:
        if pes[1] > ma:
            ma = pes[1]
        if pes[1] < me:
            me = pes[1]
    lista_pes.append(pes[:])
    pes.clear()
    res = input("Cadastras outro competidor? [S/N]").strip()[0]
    if res in "Nn":
        break
print(f"São {len(lista_pes)} o total de competidores. ")
print(f"Maior peso é {ma} Kg. e pertence á, ", end="")
for p in lista_pes:
    if p[1] == ma:
        print(p[0], end="... ")
print(f"\nMenor peso é {me} Kg. e pertence á, ", end="")
for p in lista_pes:
    if p[1] == me:
        print(p[0], end="... ")
