def ano(s):
    from datetime import date
    h = date.today().year
    idade = h - s
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif 18 <= idade < 65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    else:
        return f"Com {idade} anos: VOTO OPCIONAL"


print(ano(int(input("Ano de nascimento? "))))
