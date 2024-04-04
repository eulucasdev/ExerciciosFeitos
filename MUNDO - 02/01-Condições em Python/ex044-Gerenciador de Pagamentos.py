pro = float(input("Preço do produto R$ "))
(print("Forma de pagamento?\n"
       "[1] - DINHEIEO/PIX    |  [3] - 2xCRÉDITO\n"
       "[2] - DÉBITO/1xCARTÃO |  [4] - 3xMAIS CARTÃO"))
pag = int(input())
if pag == 1 or pag == 2 or pag == 3:
    if pag == 1:
        des = pro / 100 * 10
    elif pag == 2:
        des = pro / 100 * 5
    elif pag == 3:
        des = 0
    print(f"Você ganhou R$ {des:.2f} de desconto!\nO valor total a pagar é de R$ {pro-des:.2f}")
elif pag == 4:
    jur = pro * 20 / 100
    print(f"Com parcelas acima de 2x há um juros de R$ {jur:.2f}\n O total a pagar é de R$ {pro+jur:.2f}")
else:
    print("ERRO! - OPÇÃO INVALIDA - \n TENTE NOVAMENTE")
