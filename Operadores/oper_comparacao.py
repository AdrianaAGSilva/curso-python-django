"""
Retornam valores booleanos (True ou False) comparando dois operandos.

==  (igualdade)
!=  (diferença)
>   (mais que)
<   (menos que)
>=  (maior ou igual)
<=  (menor ou igual)
"""

# Exemplo

a, b = 10, 20
print(a == b)   # false
print(a != b)   # true
print(a < b)    # true


"""
Estudo sobre o tema:

Os Operadores de Comparação são essenciais para tomar decisões no código — como quando usamos if, while, etc.
São usados para comparar dois valores e o resultado é sempre um valor booleano:

True (verdadeiro)

ou False (falso)

            Tabela dos principais operadores de comparação:
| Operador | Significado      | Exemplo (x = 5)   | Resultado |
| -------- | ---------------- | ----------------- | --------- |
|   ==     | Igual a          |     x == 5        |   True    |
|   !=     | Diferente de     |     x != 3        |   True    |
|   >      | Maior que        |     x > 2         |   True    |
|   <      | Menor que        |     x < 10        |   True    |
|   >=     | Maior ou igual a |     x >= 5        |   True    |
|   <=     | Menor ou igual a |     x <= 4        |   False   |


Exemplo prático com if:

idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

    
Quando usar?
Sempre que você quiser:

- Comparar dois valores
- Verificar condições para decidir se algo deve ou não acontecer

Muito usado em:

if, elif, else
while
Filtros, validações, menus, jogos, etc.
"""
