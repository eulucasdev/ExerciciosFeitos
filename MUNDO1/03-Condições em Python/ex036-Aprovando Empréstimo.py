print("\033[1:34m$°\033[m"*15)
print(f"{"\033[1:33:40mENDIVIDADOR\033[m":^43}")
print("\033[1:34m$°\033[m"*15)
vc = float(input("Qual o valor da casa: R$  "))
sal = float(input("Qual seu salário atual: R$ "))
an = int(input("Em quantos anos vai pagar: "))
pres = vc / (an * 12)
por = sal / 100 * 30
if pres <= por:
    res = "\033[1:35:40mAPROVADO! Parabéns.\033[m"
else:
    res = "\033[1:31:40mNEGADO! A prestação excede 30% do seu salário.\033[m"
print("=-"*15)
print(f'Situação do empréstimo: {res}\n'
      f'Uma casa de R$ {vc:.2f} em {an} anos, a prestação seria de R$ {pres:.2f}')
