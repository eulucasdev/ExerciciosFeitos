print("$*"*15)
print(f"{"TROXABANCO":^30}")
print("$*"*15)
sac = int(input("\nQuanto vai sacar: "))
tot = sac
nota = 50
totnota = 0
print("\nVocê vai retirar: ")
print("-="*15)
while True:
    if tot >= nota:
        tot -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f"{totnota} notas de R$ {nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if tot == 0:
            break
print("-="*15)
print("Obrigado, volte sempre!")
