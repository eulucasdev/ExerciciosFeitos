tot = mmil = mval = 0
pmval = " "
while True:
    sn = " "
    prod = input("PRODUTO: ")
    valor = float(input("Valor R$: "))
    tot += valor
    while sn not in "sn":
        sn = input("Adicionar outro produto? [S/N]").strip().lower()[0]
    print(".°"*15)
    if valor > 1000:
        mmil += 1
    if mval == 0 or mval < valor:
        mval = valor
        pmval = prod
    if sn == "n":
        break
print(f"TOTAL A PAGAR: {tot:.2f}\n")
print(f"Há {mmil} produtos acima de R$ 1000,00." if mmil >= 1 else "Sem produtos a cima de R$ 1000,00.")
print(f"\nO Produto mais barato é, {pmval.upper()}")


