print("¨"*30)
print(f"{"CÁLCULO DE IMC":^30}")
print(f"¨"*30)
pes = float(input("Informe o peso em Kg: "))
alt = float(input("Informa a Altura: "))
imc = pes / (alt * alt)
if imc < 18.5:
    r = "ABAIXO do peso ideal"
elif imc < 25:
    r = "com o peso IDEAL"
elif imc < 30:
    r = "com SOBREPESO"
elif imc < 40:
    r = "com OBSIDADE"
else:
    r = "com OBESIDADE MÓRBIDA"
print(f"O seu IMC é: {imc:.1f} e você está {r}")
