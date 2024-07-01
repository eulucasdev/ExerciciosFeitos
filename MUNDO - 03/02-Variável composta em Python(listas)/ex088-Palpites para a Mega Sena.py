from random import randint

print("\33[1;32m$\33[m" * 29)
print(f"\33[1;32m$\33[1;32m{'  NÚMERO MÁGICO \33[1:33mMEGA-SENA  ':^30}$")
print("$" * 29)
jogo = list()
x = int(input("\n\33[1;37;40mQuantos jogos vai fazer?\33[m "))
for j in range(0, x):
    if j % 2 == 0:
        print("\33[1;35m")
    else:
        print("\33[1;34m")
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        jogo.sort()
    print(f"{j+1}°-JOGO:")
    for n in jogo:
        print(f"[{n:>2}]", end=" ")
    print()
    jogo.clear()
