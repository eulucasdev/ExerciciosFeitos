n1 = float(input("Primeira reta: "))
n2 = float(input("Segunda reta: "))
n3 = float(input("Terceira reta: "))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    r1 = "Esse triângulo e"
    if n1 == n2 == n3:
        r2 = "EQUILÁTERO: todos os lados iguais"
    elif n1 == n2 != n3 or n2 == n3 != n1 or n3 == n1 != n2:
        r2 = "ISÓSCELES: dois lados iguais, um diferente"
    else:
        r2 = "ESCALENO: todos os lados diferentes"
    print(r1, r2)
