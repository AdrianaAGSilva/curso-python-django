"""
Quando há várias condições que não podem ser verdadeiras ao mesmo tempo, use elif (else if).
"""

# Exemplo: faixa etária

idade = int(input("Idade: "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")