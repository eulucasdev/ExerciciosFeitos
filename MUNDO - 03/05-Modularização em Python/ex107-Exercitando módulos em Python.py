from uteis.numeros.moeda import dobro, metade, aumentar

preço = float(input("Digite um preço: "))
print(f"A metade de R$ {preço} é {metade(preço)}")
print(f"O dobro de R$ {preço} é {dobro(preço)}")
print(f"Aumentando em 10%, fica R$ {aumentar(preço, 10)}")
