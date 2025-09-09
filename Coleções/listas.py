"""
    Listas

Mutabilidade: Mutável, permitindo adição, remoção ou alteração de elementos. 
Ordenação: Mantêm a ordem de inserção. 
Indexação: Acessadas por índices inteiros (base 0). 
Flexibilidade: Suportam elementos heterogêneos.

-> Listas: Sequências mutáveis que armazenam elementos ordenados de qualquer tipo.

***Listas são criadas com colchetes ([]) ou a função list(). Eles suportam métodos como anexar, pop, inserir e remover.***

Listas: Indicadas para listas de tarefas, históricos de transações ou dados planejados que mudam frequentemente.
"""

# Exemplo 1: Gerenciamento de tarefas

tarefas = ["Estudar Python", "Fazer compras", "Enviar e-mail"]
tarefas.append("Reunião às 14h")    # Adiciona ao final
tarefas.remove("Fazer compras") # Remove elemente específico
tarefas[1] = "Enviar e-mail urgente"    # Altera elemento
print(tarefas) # saída: ['Estudar Python', 'Enviar e-mail urgente', 'Reunião às 14h']


# Exemplo 2: Filtragem de números pares

numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]
print(pares)    # Saída: [2, 4, 6]