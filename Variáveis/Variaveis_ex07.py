# Peça ao usuário a quantidade de degraus de uma escada e a altura de cada degrau. Calcule a altura total da escada.

quant_degraus = int(input("Qual a quantidade de degraus? "))
alt_degraus = float(input("Qual a altura de cada degrau? "))

alt_total = alt_degraus * quant_degraus

print(f"A altura total da escada é de {alt_total}.")