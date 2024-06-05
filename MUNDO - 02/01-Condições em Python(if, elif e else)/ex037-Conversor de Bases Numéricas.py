print('\033[1;35m><'*10)
print(f"{'CONVERSOR':^20}")
print('><'*10)
num = int(input("\033[mEntre com um número inteiro: "))
print(f"Converter {num} para?\n1 - BINÁRO\n2 - OCTAL\n3 - HEXADECIMAL")
esc = int(input())
if esc == 1:
    r1 = "BiNÁRIO"
    r2 = bin(num)
elif esc == 2:
    r1 = "OCTAL"
    r2 = oct(num)
elif esc == 3:
    r1 = "HEXADECIMAL"
    r2 = hex(num)
else:
    r1 = "ENTRADA"
    r2 = "INVÁLIDA"
    print("TENTE NOVAMENTE")
print(f"O número \033[1;32m{num}\033[m em \033[1;32m{r1}\033[m é: \033[1;32m{r2}\033[m")
