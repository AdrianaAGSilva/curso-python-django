# Solicite litros de combustível e a distância percorrida. Calcule o consumo médio (km/litro).

litros_comb = float(input("Quantos litros de combustível? "))
dist_percorrida = float(input("Qual a distância percorrida? "))

consumo = dist_percorrida / litros_comb

print(f"O consumo médio km/litro é de {consumo} km/litro.")