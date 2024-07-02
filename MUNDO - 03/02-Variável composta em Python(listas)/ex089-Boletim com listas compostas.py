alunos = list()
while True:
    temp = list()
    temp.append(str(input("Nome: ").title().strip()))
    temp.append(float(input("1° NOTA: ")))
    temp.append(float(input("2° NOTA: ")))
    alunos.append(temp[:])
    temp.clear()
    res = str(input("Cadastrar outro aluno? ")).strip().lower()[0]
    while res not in "sn":
        res = str(input("ENTRADA INVALIDA! ...RESPONDA [S/N]:")).strip().lower()[0]
    if res in "n":
        break
print("=-"*15)
print(f"{'N°'}  {'NOME':}        {'MÉDIA'}")
print("-"*30)
for i, v in enumerate(alunos):
    print(f"{i:<4}{v[0]:<8}{f"{(v[1]+v[2])/2:.1f}":>8}")
print("--"*15)
while True:
    c = 0
    print(f"{'999 PARA ENCERRAR':^30}")
    bus = str(input("Ver detalhes de qual aluno: ")).strip().title()
    print("=-"*15)
    print(f"{'N°'}  {'NOME':}        {'MÉDIA'}")
    print("-"*30)
    for i, v in enumerate(alunos):
        print(f"{i:<4}{v[0]:<8}{f"{(v[1]+v[2])/2:.1f}":>8}")
    print("--"*15)
    for aluno in alunos:
        if bus == aluno[0]:
            print(f"\n{aluno[0]} tirou as notas: {aluno[1]} e {aluno[2]}\n")
            c = 1
    if c == 0:
        if bus == "999":
            break
        print(f"\nO aluno {bus.upper()} não está cadastrado!!!\n")
        r = input(f"Deseja cadastrar {bus.title()}?").lower().strip()[0]
        if r == "s":
            temp = list()
            temp.append(bus.title())
            temp.append(float(input(f"1° NOTA de {bus}: ")))
            temp.append(float(input(f"2° NOTA de {bus}: ")))
            alunos.append(temp[:])
            temp.clear()
    if bus == "999":
        break
    print("-="*15)
print("\nPROGRAMA FINALIZADO")
