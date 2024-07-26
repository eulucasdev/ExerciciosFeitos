def escreva(txt):
    a = len(txt) + 4
    print("~"*a)
    print(f"  {txt}")
    print("~"*a)


escreva(input("Entre com seu texto: "))
