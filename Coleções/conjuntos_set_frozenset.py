"""
    Conjuntos (set e frozenset)

Mutabilidade: set é mutável; frozenset é imutável.
Ordenação: Não ordenado, sem suporte a indexação. 
Unicidade: Garantir elementos únicos, eliminando duplicatas. 
Operações: Apoiar operações de conjunto (união, interseção, diferença).

-> Conjuntos (set e frozenset): Coleções não ordenadas de elementos únicos, ideais para operações matemáticas.

***Conjuntos são criados com chaves ({}) ou set(). Métodos como adição, união e intersecção são comuns.***

Conjuntos: Aplicáveis para eliminar duplicatas (ex.: lista de e-mails únicos) ou comparar grupos (ex.: interesses comuns).
"""

# Exemplo 1: Eliminação de duplicatas

emails = ["ana@ex.com", "bob@ex.com", "ana@ex.com"]
emails_unicos = set(emails)     # set(): cria uma coleção de itens únicos, forma mais eficiente de remover elementos duplicados de uma lista.
print(emails_unicos)    # Saída: {'ana@ex.com', 'bob@ex.com'}


# Exemplo 2: Interseção de interesses

interesses_ana = {"Python", "Java", "SQL"}
interesses_bob = {"Python", "C++", "SQL"}
comuns = interesses_ana & interesses_bob    # &: Este é o operador de interseção. Compara os dois conjuntos e cria um novo conjunto contendo apenas os elementos que estão presentes em ambos.
print(comuns)   # Saída: {'Python', 'SQL'}


