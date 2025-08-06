"""
Também chamados de laços dentro de laços.
Ferramenta poderosa quando você precisa trabalhar com repetições duplas, como linhas e colunas, listas dentro de listas, tabuadas, etc.

São estruturas de repetição dentro de outras estruturas de repetição.
"""

# Exemplo: Matriz (lista de listas)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]          # lista de listas

for linha in matriz:            # pega uma linha por vez da matriz (ou seja, cada sublista): Se a linha for [1, 2, 3], esse for vai pegar 1, depois 2, depois 3.
    for elemento in linha:      # para cada linha, ele percorre cada elemento dentro dela. Se a linha for [1, 2, 3], esse for vai pegar 1, depois 2, depois 3.
        print(f"Elemento: {elemento}")      # A cada iteração do laço interno, imprime o número atual.


"""
Em resumo:
Você tem uma matriz 3x3

O primeiro for percorre as linhas

O segundo for percorre os valores dentro de cada linha

E imprime cada valor separadamente
"""