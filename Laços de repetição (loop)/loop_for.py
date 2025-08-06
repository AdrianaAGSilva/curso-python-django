"""
Tradução: for = "para"

É uma estrutura de repetição usada para percorrer sequências (listas, strings, ranges, etc.)

Permite executar um bloco de código para cada item da sequência.

Evita escrever comandos repetidos manualmente.

Estrutura básica:
for variavel in sequencia:          # bloco de código a ser executado

Significa:
Para cada item da sequência, guarde esse item na variável e execute o que estiver dentro do bloco.
"""

# Exemplos 1: Iterando uma lista

frutas = ["maca", "uva", "morango", "laranja", "banana"]
for fruta in frutas:
    print(f"Frutas: {fruta}")


# Exemplo 2: Iterando sobre um conjunto
"""
Conjuntos (set) são coleções não ordenadas de elementos únicos. O laço for pode ser usado para percorrer seus elementos, mas a ordem não é garantida.
"""

numeros = [1, 2, 3, 4, 5, 6]
for num in numeros:
    print(f"Número: {num}")


# Exemplo 3: Usando range()para números
"""
O range() é uma função que gera uma sequência de números, ideal para iterações baseadas em índices.
"""

for i in range (5):    # Gera números de 0 a 4
    print(f"índice: {i}")
