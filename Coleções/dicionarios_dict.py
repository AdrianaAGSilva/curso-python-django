"""
    Dicionários

Mutabilidade: Mutável, permitindo manipulação de pares chave-valor.
Ordenação: Desde Python 3.7, preserva a ordem de inserção. 
Indexação: Acessados por chaves imutáveis (ex.: strings, números, tuplas). 
Eficiência: Otimizado para buscas rápidas por chave.

-> Dicionários (dict): Estruturas de pares chave-valor, otimizadas para buscas por chave.

**Dicionários são criados com chaves ({}) ou dict(). Métodos como get, update e pop facilitam manipulações.***

Dicionários: Ideais para cadastros (ex.: informações de clientes por ID) ou contagens de frequência.
"""

# Exemplo 1: Cadastro de produto 

produto = {"id": 101, "nome": "Notebook", "preco": 3500.00}
produto["estoque"] = 10     # Adiciona nova chave
produto.update({"preco": 3400.00, "marca": "Tech"})    # Atualiza múltiplos valores
print(produto.get("nome", "Desconhecido"))    # Saída: Notebook


"""
    método .get()

O método .get() é uma forma de acessar o valor de uma chave em um dicionário. A grande vantagem dele em relação ao acesso direto (como produto["nome"]) é como ele lida com chaves que não existem.

O método .get() aceita dois argumentos:

1. A chave que você quer buscar (obrigatório).
2. Um valor padrão para retornar caso a chave não seja encontrada (opcional).

Vamos quebrar a sua linha em partes:

produto.get(...): Estamos chamando o método .get() no nosso dicionário produto.

"nome": Este é o primeiro argumento. Estamos pedindo ao método para buscar a chave "nome" dentro do dicionário produto.

"Desconhecido": Este é o segundo argumento, o valor padrão. Ele serve como um "plano B". A instrução é: "se você não encontrar a chave "nome", não gere um erro; em vez disso, me retorne a string "Desconhecido"".
"""

# Exemplo 2: Contagem de ocorrências

frases = ["gato", "cachorro", "gato", "pássaro"]
contagem = {}       # {}: Esta é a sintaxe literal em Python para criar um dicionário vazio. É um atalho para dict().
for palavra in frases:
    contagem[palavra] = contagem.get(palavra, 0) + 1
    print(contagem)     # Saída: {'gato': 2 'cachorro': 1, 'pássaro': 1}


