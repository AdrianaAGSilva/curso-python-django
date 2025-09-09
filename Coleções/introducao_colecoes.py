"""
Coleções:

Uma coleção é um objeto que organiza múltiplos elementos em uma estrutura coesa, permitindo manipulações eficientes. Python implementa coleções como tipos embutidos, projetados para flexibilidade e desempenho. As principais coleções incluem:

Listas: Sequências mutáveis que armazenam elementos ordenados de qualquer tipo.

Tuplas: Sequências imutáveis que mantêm a ordem dos elementos.

Dicionários (dict): Estruturas de pares chave-valor, otimizadas para buscas por chave.

Conjuntos (set e frozenset): Coleções não ordenadas de elementos únicos, ideais para operações matemáticas.

Arrays (array.array): Estruturas convencionais do módulo array, otimizadas para eficiência de memória.

Cada coleção possui características específicas que determinam sua adequação a diferentes problemas, como ordenação, mutabilidade e eficiência computacional.

                            Tabela Comparativa:

| Estrutura                 | Ordem              | Mutabilidade      | Duplicatas        | Acesso       | Uso Principal                        |
|---------------------------|--------------------|-------------------|-------------------|--------------|--------------------------------------|
| Lista (list)              | Ordenada           | Mutável           | Permite           | Índice       | Sequências dinâmicas de uso geral    |
| Tupla                     | Ordenada           | Imutável          | Permite           | Índice       | Dados que não devem mudar            |
| Dicionário (dict)         | Ordenado (moderno) | Mutável           | Chaves únicas     | Chave        | Associações chave-valor              |
| Conjunto (set e frozenset)| Não Ordenado       | Mutável           | Não Permite       | Verificação  | Garantir unicidade                   |
| Array (array.array)       | Ordenado           | Imutável (tamanho)| Permite           | Índice       | Dados homogêneos, tamanho fixo       |


Casos de Uso:

Listas: Indicadas para listas de tarefas, históricos de transações ou dados planejados que mudam frequentemente.

Tuplas: Usadas para configurações fixas, como conexões de banco de dados (host, porta, usuário) ou coordenadas.

Dicionários: Ideais para cadastros (ex.: informações de clientes por ID) ou contagens de frequência.

Conjuntos: Aplicáveis para eliminar duplicatas (ex.: lista de e-mails únicos) ou comparar grupos (ex.: interesses comuns).

Matrizes: Recomendados para processamento numérico intensivo, como análise de dados sensoriais ou cálculos estatísticos.
Um Array é uma estrutura de dados da programação que usamos para representar uma matriz.
"""