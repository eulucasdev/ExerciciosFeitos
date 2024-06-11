es = input("Digite a expressão: ")
c = []
for sim in es:
    if sim == "(":
        c.append("(")
    elif sim == ")":
        if len(c) > 0:
            c.pop()
        else:
            c.append(")")
            break
if len(c) == 0:
    print(f"A expressão {es} está CORRETA ")
else:
    print("INCORRETO")
