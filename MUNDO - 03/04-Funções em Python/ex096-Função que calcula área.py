def tit(txt):
    print("="*30)
    print(f"{txt:^30}")
    print("="*30)

def area(a, b):
    t = a * b
    print("=-"*15)
    print(f"\nA área desse terreno é de {t:.1f}m².")


tit("CONTROLE DE TERRENOS")
area(a=float(input("LARGURA (m): ")), b=float(input("COMPRIMENTO (m): ")))
