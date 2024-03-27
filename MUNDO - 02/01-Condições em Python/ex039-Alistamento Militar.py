from datetime import date
ano = date.today().year
print("\033[1:32m", "°*"*15)
print(f"{"BOLD FORCES":^30}")
print("*°"*15, "\033[m")
n = int(input("Em que ano nasceu: "))
idade = ano - n
if 17 <= idade < 19:
    print("\033[1:33mCORRA!\33[m Está na hora de se alistar! ")
elif idade <= 16:
    print(f"\33[1;32mCALMA JOVEM,\33[m Ainda faltam \33[1:32m->{18-idade}<-\033[m para poder se alistar!")
else:
    print(f"\33[1:31mMUITO ATRASADO!\33[m Você deveria ter se alistado a {idade-18} ano(s)!")
