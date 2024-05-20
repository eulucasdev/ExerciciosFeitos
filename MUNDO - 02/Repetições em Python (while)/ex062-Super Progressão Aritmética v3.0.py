print("GERADOR DE P.A")
print("=-" * 15)
t = int(input("Digite o 1° termo: "))
r = int(input("Digite a razão: "))
c = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while c <= tot:
        print(f"{t} -> ", end="")
        t += r
        c += 1
    print("PAUSA")
    mais = int(input("Mostrar mais quantos termos? "))
print("-="*15)
print(f"Passados o total de {tot} termos.\nProgressão finalizada!")
