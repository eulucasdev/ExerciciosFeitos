CBF24 = ("Athletico-PR", "Bahia", "Flamengo", "Botafogo", "São Paulo",
            "Cruzeiro", "Atlético-MG", "Bragantino", "Palmeiras", "Internacional",
            "Fortaleza", "Grêmio", "Vasco", "Criciúma", "Juventude",
            "Corinthians", "Fluminense", "Vitória", "Atlético-GO", "Cuiabá")
print(f"\n\nCampeonato Brasileiro de Futebol:\n{CBF24}")
print("-="*15)
print(f"\n\nOs cinco primeiros:\n{CBF24[:5]}")
print("-="*15)
print(f"\n\nOs quatro últimos:\n{CBF24[-4:]}")
print("-="*15)
print(f"\n\nEm ordem alfabética: \n{sorted(CBF24)}")
print("-="*15)
print(f"\n\no Vasco se encontra na: \n{CBF24.index("Vasco")+1}° Posição")
