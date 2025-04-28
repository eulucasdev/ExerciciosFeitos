from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = "registro.txt"
if not existe(arq):
    criararquivo(arq)
while True:
    resposta = menu(["LISTAR PESSOAS","CADASTRAR PESSOAS", "SAI DO SISTEMA"])
    if resposta == 1:
        cabeçalho("PESSOAS CADASTRADAS")
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho("CADASTRAR NOVA PESSOA")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite um valor valido!\033[m")
        sleep(2)
