def existe(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("ERRO ao criar arquivo")
    else:
        print(f"Arquivo {nome}, criado com sucesso!")


def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("ERRO! ao ler arquivo")
    else:
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Erro ao abrir arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Erro! ao escrever arquivo")
        else:
            print("Novo cadastro efetuado")
            a.close()