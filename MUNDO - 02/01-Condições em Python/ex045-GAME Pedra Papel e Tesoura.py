from random import randint
jok = ["pedra", "papel", "tesoura"]
pc = randint(0, 2)
jog = int(input("[1] - Pedra, [2] - Papel, [3] - Tesoura? "))-1
if pc == jog:
    r = "EMPATE! ninguém ganhou!"
elif pc > jog:
    r = "Que pena você PERDEU!"
else:
    r = "Você GANHOU! Parabéns"
print(f"Você escolheu: {jok[jog]} e eu escolhi {jok[pc]}\n{r}")


