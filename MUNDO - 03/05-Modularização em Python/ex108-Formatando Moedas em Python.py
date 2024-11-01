from uteis.numeros.moeda import dobro, metade, aumentar, real

preço = float(input("Digite um preço: "))
print(f"A metade de {real(preço)} é {real(metade(preço))}")
print(f"O dobro de {real(preço)} é {real(dobro(preço))}")
print(f"Aumentando em 10%, fica {real(aumentar(preço, 10))}")
