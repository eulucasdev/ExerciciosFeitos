e = int(input("Devo somar até qual número: "))
im3 = 0
c = 0
for n in range(1, e+1, 2):
    if n % 3 == 0:
        im3 += n
        c += 1
print(f"A somas dos {c} números impares mutiplos de 3 é: {im3}")
