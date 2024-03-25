print("-"*30)
print(f"{"PARA PINTAR BASTA CALCULAR":^30}")
print("-"*30)

l = float(input("Qual a LARGURA em metros? "))
a = float(input("Qual a ALTURA em metros? "))
t = float(input("Quantos m² 1L da tinta cobre? "))
al = l*a
print("-="*20)
print(f"Sua área tem {al:.1f}m² e para pintala\nvocê vai usar {al/t:.1f} litros de tinta.")
