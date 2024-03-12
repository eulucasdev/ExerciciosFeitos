from time import sleep
from random import randint
print("\33[0;33m-=\33[m"*25)
print("\33[0;34mQual número entre 0 e 5 estou pensando?\33[m")
print("\33[0;33m-=\33[m"*25)
pc = randint(0, 5)
p1 = int(input("Em que número pensei? "))
print("\33[0;35mPROCESSANDO...\33[m")
sleep(2)
if p1 == pc:
    r = f"\33[0;32mParabéns, eu pensei no número {pc}!\33[m"
else:
    r = f"\33[0;31mGanhei! Eu pensei no número {pc} e não no {p1}.\33[m"
print(r)
