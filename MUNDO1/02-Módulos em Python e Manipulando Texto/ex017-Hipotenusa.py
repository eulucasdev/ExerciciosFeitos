from math import hypot
print("MEDINDO A HIPOTENUSA ")
print("="*35)
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hip = hypot(co, ca)
print("="*35)
print(f"A hipotenusa é de: {hip:.2f}")
