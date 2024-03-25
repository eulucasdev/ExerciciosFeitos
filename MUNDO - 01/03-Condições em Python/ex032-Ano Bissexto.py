print("*"*25)
print(f'\033[0;35m{"ESSE ANO É BISSEXTO?":^25}\033[m')
print(f"*"*25)
ano = int(input("Entre com um ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    r = f"O ano de {ano} \033[0;34mÉ bissexto\033[m"
else:
    r = f"O ano de {ano} \033[0;31mNÃO é bissexto\033[m"
print(r)

