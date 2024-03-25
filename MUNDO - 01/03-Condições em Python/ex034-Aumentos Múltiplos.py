sa = float(input("Salário atual? "))
if sa <= 1250.00:
    por = sa / 100 * 15
else:
    por = sa / 100 * 10

print(f"Você vai receber um aumento de \033[1:33m{por/10:.0f}%\033[m."
      f"\nSeu novo salário é de:\033[1:32m R$ {sa+por:.2f}\033[m")
