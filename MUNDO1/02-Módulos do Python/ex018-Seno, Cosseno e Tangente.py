from math import radians, sin, cos, tan
a = float(input("Qual o ângulo desejado? "))
print("¨"*30)
print(f"{f"O ângulo de {a:.2f} tem ":^30}")
print("¨"*30)
print(f"SENO: {sin(radians(a)):>10.2f}\n"
      f"COSSENO: {cos(radians(a)):>7.2f}\n"
      f"TANGENTE: {tan(radians(a)):>6.2f}")
