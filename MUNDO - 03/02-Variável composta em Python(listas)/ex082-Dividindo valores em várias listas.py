val = []
par = []
imp = []
while True:
    val.append(int(input("Entre com um número inteiro: ")))
    res = input("INSERIR OUTRO VALOR? [S/N]").strip()[0]
    if res in "nN":
        break
for v in val:
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
print("-="*15)
val.sort()
par.sort()
imp.sort()
print(f"Os números digitados foram: {val}\n"
      f"Os pares são: {par}\n"
      f"Os impares são: {imp}")
