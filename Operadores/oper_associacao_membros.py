"""
Verifiquem se um valor está presente em uma sequência (string, lista, tupla, etc.).

in
not in
"""

# Exemplo

texto = "Olá, mundo!"
print("mundo" in texto)    # true
print(42 not in [1, 2, 3])  # true


"""
Estudo sobre o tema:

Eles verificam se um valor está ou não está dentro de uma sequência (lista, string, tupla, etc).

            Tabela dos dois operadores:

| Operador | Significado                      | Exemplo              | Resultado |
| -------- | -------------------------------- | -------------------- | --------- |
|  in      | Está dentro / pertence a         |  "a" in "banana"     |  True     |
|  not in  | Não está dentro / não pertence a |  5 not in [1, 2, 3]  |  True     |


Exemplos simples

Com strings:

"vin" in "vinne"       # True
"a" not in "banana"    # False


Com listas:

frutas = ["maçã", "banana", "uva"]

"maçã" in frutas       # True
"melancia" in frutas   # False


Quando usar?

Para "verificar se algo existe" dentro de uma sequência.

Muito comum em:
- Validação de entrada
- Filtros
- Pesquisas em listas
- Checagem de palavras em textos

Dica:
Você pode usar com qualquer tipo de estrutura iterável (string, lista, tupla, dicionário - nesse caso com as chaves).


"""