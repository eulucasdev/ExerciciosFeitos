n = int(input("\033[1;31;46mEscolha um número inteiro:\033[m "))
if n % 2 == 0:
    r = f"O número {n} é \033[2;32;40mPAR\033[m"
else:
    r = f"O úmero {n} é \033[3;30;47mÍMPAR\033[m"
print("\n",r)
