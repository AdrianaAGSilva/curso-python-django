"""
Permitem combinar expressões booleanas.

and (E)
or  (OU)
not (NÃO)
"""

# Exemplo

idade = 25
saldo = 1500

# True se idade for entre 18 e 65 E saldo >= (1000
aprovado = (idade >= 18 and idade <= 65) and (saldo >= 1000)
print("Aprovado!") # true

"""
Estudo sobre o tema:

São essenciais quando você quer combinar várias comparações ao mesmo tempo — e tomar decisões mais inteligentes no código.

Eles permitem combinar condições (True ou False) usando:

| Operador | Nome       | O que faz                                                   |
| -------- | ---------- | ----------------------------------------------------------- |
|  and     | E lógico   | Só é `True` se **todas** as condições forem verdadeiras     |
|  or      | OU lógico  | É `True` se **pelo menos uma** das condições for verdadeira |
|  not     | NÃO lógico | Inverte o valor: `True` vira `False`, e vice-versa          |


and - todas as condições precisam ser verdadeiras:

idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")

Só imprime se as duas forem verdadeiras.   


or - basta uma condição verdadeira:

tem_dinheiro = False
tem_cartao = True

if tem_dinheiro or tem_cartao:
    print("Pode fazer a compra.")

Vai imprimir porque tem_cartao é True, mesmo sem dinheiro.


not - inverte o valor:

tem_multas = False

if not tem_multas:
    print("Você está regularizado.")

not False vira True, então a mensagem aparece.
"""