# Peça ao usuário o valor de uma compra e o percentual de desconto. Calcule o valor final com desconto.

valor_compra = float(input("Qual o valor da compra? "))
perc_desconto = int(input("Qual percentual do desconto? "))

valor_final = valor_compra * perc_desconto / 100

print(f"O valor final com desconto é de R${valor_final}")
