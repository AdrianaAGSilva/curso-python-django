"""
O if disponível é uma condição booleana e executa um bloco de código apenas se ela
for verdadeira.
"""

# Exemplo 1: verifique se um número é par

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print(f"{num} é par!")


# Exemplo 2: aplicar desconto genérico

valor = float(input("Valor da compra: R$ "))
if valor > 100:
    print("Você ganhou 10% de desconto!")

        
