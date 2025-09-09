"""
    Arrays (array.array) ?????????????

Matrizes: ???????????????????????????????/

Mutabilidade: Mutável, mas restrita a tipos homogêneos. 
Ordenação: Mantêm a ordem dos elementos. 
Eficiência: Otimizados para dados numéricos, consumindo menos memória que listas.


-> Arrays (array.array): Estruturas convencionais do módulo array, otimizadas para eficiência de memória.

***O módulo array cria arrays homogêneos, especificando o tipo de dado (ex.: 'i' para inteiros) da matriz importar matriz.***

Matrizes: Recomendados para processamento numérico intensivo, como análise de dados sensoriais ou cálculos estatísticos.
Um Array é uma estrutura de dados da programação que usamos para representar uma matriz.
"""

# Exemplo 1: Armazenamento de temperaturas

from array import array

temperaturas = array('f', [23.5, 24.0, 22.8])
temperaturas.append(25.1)
print(temperaturas)     # Saída: array('f', [23.5, 24.0, 22.8])

#  Exemplo 2: Cálculo de média

media = sum(temperaturas) / len(temperaturas)
print(f"Média: {media:.2f}")    # Saída: Média: 23.85