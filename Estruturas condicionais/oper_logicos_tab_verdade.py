"""
Operadores Lógicos e Tabela Verdade
Operadores que combinam expressões booleanas (verdadeiras ou falsas) e retornam um resultado lógico (True ou False).

and (E lógico)
or (OU lógico)
not (NÃO lógico)

Resumo das Regras:
and → verdadeiro somente se ambos forem True;
or → verdadeiro se qualquer um for True;
not → inverte o valor lógico.

                Tabela Verdade

| A     | B     | A and B | A or B | not A |
| ----- | ----- | ------- | ------ | ----- |
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |
"""

x = int(input("Número: "))          # Pede ao usuário que digite um número.
if 0 <= x <= 50:                    # Comparação encadeada, verifica duas coisas ao mesmo tempo, x >= 0 (x é maior ou igual a zero) - x <= 50 (x é menor ou igual a cinquenta).
    print("Está entre 0 e 50")      # Se x estiver entre 0 e 50, inclusive, essa condição será True.
else:
    print("Fora do intervalo")