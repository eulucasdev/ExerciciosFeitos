nome = input("Digite seu nome completo: ").strip()
a = nome.split()
print(f"Seu primeiro nome é: {a[0].title()}\n"
      f"Seu último nome é: {a[-1].title()}")
#print(f"Seu último nome é: {a[len(a)-1].title()}")
