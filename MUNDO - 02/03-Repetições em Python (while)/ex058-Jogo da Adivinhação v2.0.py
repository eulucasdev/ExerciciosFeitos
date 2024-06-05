from random import randint
comp = randint(0, 10)
jog = int(input("Qual número entre 0 a 10 estou pensando? "))
tent = 1
while comp != jog:
    tent += 1
    if jog > comp:
        jog = int(input("MENOS! Tente novamente: "))
    elif jog < comp:
        jog = int(input("MAIS! Tente novamente: "))
print(f"Parabéns! após á {tent}° tentativa você acertou.")