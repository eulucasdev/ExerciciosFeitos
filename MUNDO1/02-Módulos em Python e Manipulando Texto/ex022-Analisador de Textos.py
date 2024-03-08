nome = input("Digite o nome completo: ")
print(f"Seu nome com todas as letras maiusculas: {nome.upper()}\n"
      f"Seu nome com todas as letras minusculas: {nome.lower()}\n"
      f"Seu nome tem o total de {len(nome.replace(" ",""))}\n"
      f"Seu primeiro nome tem {len(nome.split()[0])} ")
