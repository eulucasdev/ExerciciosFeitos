pal = input("Digite a Frase: ")
pal1 = pal.replace(" ", "").lower()
pal2 = ""
for c in reversed(pal1):
    pal2 += c
print(f"A frase \33[1:35:40m{pal1}\33[m inverso é: \33[1:35:40m{pal2}\33[m\n")
if pal2 == pal1:
    print(f"Por isso \33[1:33m{pal}\33[m É um palíndromo")
else:
    print(f"Por isso \33[1:33m{pal}\33[m NÃO é um palíndromo")
