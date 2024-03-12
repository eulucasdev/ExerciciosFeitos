km = float(input("Quantos Km de viagem? "))
if km > 200:
    r = km*0.45
else:
    r = km*0.50

print(f"Sua passagem vai custar: \033[1::40mR$ {r:.2f}\033[m")
