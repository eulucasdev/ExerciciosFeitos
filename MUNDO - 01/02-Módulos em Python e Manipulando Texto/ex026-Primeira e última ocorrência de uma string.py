tex = input("Digite uma frase: ").strip().lower()
l = input("Sobre qual letra buscar informações? ")
print(f"Qantos {l.upper()} tem na frase: {tex.count(l)}\n"
      f"A primeira letra {l.upper()} aparece na posição: {tex.find(l)+1}\n"
      f"Ultima letra {l.upper()} aparece na posição: {tex.rfind(l)+1}")
