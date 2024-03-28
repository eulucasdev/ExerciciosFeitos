print("#-"*15)
print(f"{"MÉDIA DO ALUNO":^30}")
print(f"-#"*15)
nome = str(input("Nome do aluno: "))
pn = (float(input("Primeira nota: ")))
sn = (float(input("Segunda nota: ")))
media = (pn + sn) / 2
if media >= 7:
    n = "\033[1;32mAPROVADO\033[m"
elif media > 5:
    n = "de \033[1;33mRECUPERAÇÃO\033[m"
else:
    n = "\033[1;31mREPROVADO\033[m"
print(f"{nome.title()} está {n}, sua média foi: \033[1;355m{media:.2f}\033[m")
