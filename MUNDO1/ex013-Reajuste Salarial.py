sal = float(input("Qual o salário do funcionario: "))
por = float(input("Porcentagem(%) do aumento: "))
nosa = sal * por / 100
print("-="*20)
print(f"Remuneração antes do aumento R$ {sal:.2f}\n"
      f"Porcentagem do aumento {por:.2f}%\n"
      f"Valor do aumento R$ {nosa:.2f}\n"
      f"Remuneração após aumento R$ {sal+nosa:.2f}")
