"""
Tradução: while = "enquanto"

while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.

Estrutura básica:
while condicao:         # Bloco de código a ser executado

A condicaoé avaliada antes de cada iteração.
Se a condição for True, o bloco de código será executado.
Se a condição for False, o laço termina.
Cuidado: Um laço whilemal configurado pode resultar em um laço infinito.
"""

# Exemplo 1: Contagem com lista

numeros = [10, 20, 30, 40, 50, 60]      # lista de 6 elementos, com índices de 0 a 5
indice = 0
while indice < len(numeros):        # Condição do laço: executa enquanto o índice for menor que o tamanho da lista
    print(f"Elemento: {numeros[indice]}")
    indice += 1     # o indice vai aumentando de 1 em 1 até chegar ao final da lista.

# O comando len() em Python é uma função embutida que retorna o número de itens em um objeto.


# Exemplo 2: Filtrando elementos de um conjunto
"""
Filtrar significa: Selecionar apenas os itens que atendem a uma condição específica.
Por exemplo:
"Quero apenas os números maiores que 10."
"Quero só as palavras que têm mais de 5 letras."
"""

numeros = {2, 4, 6, 8, 10}
soma = 0

while numeros:
    num = numeros.pop()         # .pop() é um método que remove e retorna um item de uma estrutura de dados.
    if num % 2 == 0:            # verifica se o número armazenado na variável num é par, Verifica se o resto da divisão foi zero,
        soma += num                   # Se o número dividido por 2 tiver resto 0, então é par.
    print(f"Soma parcial: {soma}")










