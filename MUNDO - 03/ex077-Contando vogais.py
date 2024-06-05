pal = "regua", "sapato", "vassoura", "martelo", "paralelepipedo", "canteiro", "tinteiro"
print("=-"*15)
print("As vogais das palavras")
print("-="*15)
for p in pal:
    print(f"As vogais de {p.upper()} são:", end=" ")
    for v in p:
        if v.upper() in "AEIOU":
            print(v.upper(), end=". ")
    print("\n")
