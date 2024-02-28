print('-'*25)
print(f"{"TEC-MUNDO SHOP":^25}")
print('-'*25)
p = float(input("Qual valor do produto: "))
por = float(input("Porcentagem de desconto: %"))

d = p*por/100
print('-='*13)
print(f"Subtotal R$ {p:.2f}\n"
      f"Desconto R$ {d:.2f}\n"
      f"Total á pagar R$ {p-d:.2f} ")
