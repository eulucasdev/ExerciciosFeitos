from uteis.string import leiadinheiro
from uteis.numeros.moeda import resumo
v = input("Digite o valor: R$ ")
resumo(leiadinheiro(v))
