"""
Combinam uma operação aritmética com a atribuição de valor à variável.

=
+=
-=
*=
/=
//=
%=
**=
"""

# Exemplo

x = 5
x += 3  # equivalente a x = x + 3 -> x passa a valer 8
x *= 2  # x = x * 2 -> x passa a valer 16


"""
Estudo sobre o tema:

=
É o mais comum — atribui um valor direto a uma variável.

            Operadores de Atribuição Combinados
Esses fazem uma operação e atribuição ao mesmo tempo:

| Operador | Significa                 | Exemplo   | Equivalente a... |
| -------- | ------------------------- | --------- | ---------------- |
|   +=     | Soma e atribui            |  x += 5   |   x = x + 5      |
|   -=     | Subtrai e atribui         |  x -= 2   |   x = x - 2      |
|   *=     | Multiplica e atribui      |  x *= 3   |   x = x * 3      |
|   /=     | Divide e atribui          |  x /= 2   |   x = x / 2      |
|   //=    | Divisão inteira e atribui |  x //= 2  |   x = x // 2     |
|   %=     | Módulo e atribui          |  x %= 2   |   x = x % 2      |
|   **=    | Potência e atribui        |  x **= 2  |   x = x ** 2     |


Exemplo prático:

x = 10
x += 3     Agora x vale 13
x *= 2     Agora x vale 26


Quando usar?

Quando você quiser atualizar o valor de uma variável baseada nela mesma.
Muito comum em contadores, acumuladores ou laços (loops).

Exemplo:

soma = 0
soma += 5  soma agora é 5
soma += 3  soma agora é 8
"""

