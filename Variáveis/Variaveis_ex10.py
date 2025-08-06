# Solicite a largura e o comprimento de um terreno e calcule o valor total, sabendo o preço do metro.

largura = float(input("Qual a largura do terreno? "))
comprimento = float(input("Qual o comprimento do terreno? "))
preco_metro = float(input("Qual valor do metro? "))

metros_totais = largura * comprimento 

valor_total = preco_metro * metros_totais

print(f"A metragem total do terreno é de {metros_totais} metros, o valor total do terreno é de {valor_total}!")