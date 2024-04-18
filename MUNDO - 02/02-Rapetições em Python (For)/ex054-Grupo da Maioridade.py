from datetime import date
ah = date.today().year
ma = me = 0
for c in range(1, 8):
    ano = int(input(f"Ano de nascimento do participante {c}: "))
    idade = ah - ano
    if idade >= 18:
        ma += 1
    else:
        me += 1
print("-="*10)
print(f"Ao todo temos:\n"
      f"* {me} Menores de idade\n"
      f"* {ma} Maiores de idade")
