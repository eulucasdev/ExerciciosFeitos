from uteis.numeros import moeda

preço = float(input("Digite um preço: "))
print(f"A metade de {moeda.real(preço)} é {moeda.metade(preço, True)}")
print(f"O dobro de {moeda.real(preço)} é {moeda.dobro(preço, True)}")
print(f"Aumentando em 10%, fica {moeda.aumentar(preço, 10, True)}")
print(f"Diminuindo em 15%, fica {moeda.diminuir(preço, 15, True)}")
