num = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
       "treze", "quatorze", "quinze", "dezesseis", "dezessete ", "dezoito", "dezenove", "vinte")
while True:
    while True:
        ent = int(input("Entre com um número de 0 a 20: "))
        if 0 <= ent <= 20:
            break
    print(f"Você digitou o número: \033[2:35m{num[ent].upper()}\033[m")
    sn = input("Escolher outro número ? [S/N]")[0].strip()
    if sn == "n":
        break
print("Programa finalizado!")
