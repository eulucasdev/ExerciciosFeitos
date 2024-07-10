from datetime import date
a = date.today().year
tra = dict()
tra["nome"] = str(input("Nome: ").title().strip())
tra["ano"] = int(input("Ano de nascimento: "))
tra["ctps"] = int(input("Carteira de Trabalho (0 NÃO TEM): "))
if tra["ctps"] != 0:
    tra["contra"] = int(input("Ano de contratação: "))
    tra["sal"] = input("Salário: ")
    res = (f"\n- O nome é: {tra['nome']}"
           f"\n- Idade: {a - tra['ano']}"
           f"\n- Número do CTPS: {tra['ctps']}"
           f"\n- Início do contrato: {tra['contra']}"
           f"\n- Salário atual: {tra['sal']}"
           f"\n- Se aposenta aos {35-(a-tra['contra'])+(a-tra['ano'])} anos")
else:
    res = (f"\n- O nome é: {tra['nome']}"
           f"\n- Idade: {a - tra['ano']}"
           f"\n- Número do CTPS: {tra['ctps']}")
print("=-"*15)
print(res)
