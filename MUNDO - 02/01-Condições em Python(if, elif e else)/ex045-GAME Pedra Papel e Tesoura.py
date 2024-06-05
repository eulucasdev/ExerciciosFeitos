from time import sleep
from random import randint
print("-*"*15)
print(f"{"JOKEMPÔ":^30}")
print("*-"*15)
print("\33[1;35mESCOLHA COM SABEDORIA:\033[m")
jok = ["pedra", "papel", "tesoura"]
pc = randint(0, 2)
jog = int(input("[1] - Pedra\n[2] - Papel\n[3] - Tesoura\nQual a sua escolha: "))-1
if jog > 2:
    print("\33[1:30:41mERRO! OPÇÃO INVALIDA\33[m\nESCOLHA ENTRE: \33[1:30:43m[1, 2 OU 3]\33[m")
else:
    print("JO")
    sleep(0.5)
    print("KEM")
    sleep(0.5)
    print("PÔ!")
    sleep(0.5)
    if pc == jog:
        r = "e"
    elif pc == 0:
        if jog == 1:
            r = "v"
        elif jog == 2:
            r = "p"
    elif pc == 1:
        if jog == 0:
            r = "p"
        elif jog == 2:
            r = "v"
    else:
        if jog == 0:
            r = "v"
        elif jog == 1:
            r = "p"
    print(f"Você escolheu: \33[1:36m{jok[jog].upper()}\33[m.\nO Computador escolheu: \33[1:35m{jok[pc].upper()}\33[m ")
    if r == "v":
        res = "\33[1:32mVOCÊ GANHOU.\33[m"
    elif r == "p":
        res = "\33[1:31mVOCÊ PERDEU.\33[m"
    else:
        res = "\33[1:33mDEU EMPATE.\33[m"
    print(res)
