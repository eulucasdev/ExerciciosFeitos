from math import trunc
num = float(input("Digite um número real: "))
print("-="*10)
print(f"Você digitou {num} e sua porção inteira é:"
      f"\n{trunc(num)} <- Módulo math.trunc()")
print(int(num), "<- int(num) ")
