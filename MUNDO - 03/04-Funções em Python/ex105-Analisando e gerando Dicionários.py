def notas(*n, sit=False):
    """
    —> Função que retorna dados sobre notas dos alunos.
    :param n: Uma ou mais notas (aceita várias)
    :param sit: Opcional, indica se deve ou não informar a situação.
    :return: Dicionário com informações sobre as notas da turma.
    """
    res = dict()
    res["total"] = len(n)
    res['maior'] = max(n)
    res['menor'] = min(n)
    res['média'] = sum(n)/len(n)
    if sit:
        if res['média'] < 5:
            a = 'RUIM'
        elif res['média'] < 7.5:
            a = 'RAZOÁVEL'
        else:
            a = "BOA"
        res['situação'] = a
    return res


resp = notas(3.8, 1, 5.5, 2.5, 8.5, sit=True)
print(resp, help(notas))
