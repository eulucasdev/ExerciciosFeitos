aluno = {'nome': input("Nome do aluno: ").strip().title(), 'média': float(input("Média do aluno: "))}
if aluno['média'] >= 6.95:
    s = "\033[01:32mAPROVADO"
elif aluno['média'] >= 4.95:
    s = "\033[01:33mRECUPERAÇÃO"
else:
    s = "\033[01:31mREPROVADO"
print('=-'*15)
print(f" - NOME: {aluno['nome']}\n - MÉDIA:  {aluno['média']:.1f}\n - SITUAÇÃO: {s}")
