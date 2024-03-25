print("\033[1;36m.°\033[m"*15)
print(f"\033[1;33m{"GERADOR DE MULTAS":^30}\033[m")
print("\033[1;36m°.\033[m"*15)
vel = int(input("Qual a velocidade do veiculo? "))
if vel <= 80:
    r = "\033[0;32mDentro do limite! Parábens\033[m."
else:
    r = (f"\033[0;31mMULTADO! Você passou {vel-80}km acima do permitido\033[m"
         f"\n Terá que pagar R$ {(vel-80)*7:.2f}")
print(r)
