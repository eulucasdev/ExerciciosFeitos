print(f"{"P.A GERADOR":^30}")
print("-="*15)
t = int(input("Entre com o primeiro termo: "))
r = int(input("Entre com a razão: "))
c = 1
while c <= 10:
    print(t, '-> ' if c < 10 else "-> FIM!", end="")
    t += r
    c += 1
