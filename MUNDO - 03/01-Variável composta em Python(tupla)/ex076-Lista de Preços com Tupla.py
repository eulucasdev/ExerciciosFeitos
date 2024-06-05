prod = "lápis", 1.65, "borracha", 2.30, "apontador", 4.6, "bolsa", 35.78, "compasso", 5
print("-"*40)
print(f"{"COMPROVANTE DE PREÇOS":^40}")
print("-"*40)
for p in (range(0, len(prod))):
    if p % 2 == 0:
        print(f"{prod[p]:.<30}", end="")
    else:
        print(f"R${prod[p]:>7.2f}")
print("-="*20)
