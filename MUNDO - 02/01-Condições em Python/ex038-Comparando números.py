n1 = int(input("Entre com 1° número: "))
n2 = int(input("Entre com 2° número: "))
if n1 > n2:
    r = '\nO PRIMEIRO valor é maior.'
elif n1 < n2:
    r = "\nO SEGUNDO valor é maior."
else:
    r = "\nNão exixte valor maior, ambos são iguais!"
print(f"\033[2:35m{r}")
