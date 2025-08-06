# Solicite o valor de um produto e o número de parcelas. Calcule o valor de cada parcela.

valor_prod = float(input("Qual valor do produto? "))
numero_parc = int(input("Qual a quantidade de parcelas? "))

valor_parc = valor_prod / numero_parc

print(f"O valor de cada parcela é de R${valor_parc}")