"""
Operam diretamente sobre os bits de inteiros.

&   (E um pouquinho)
|   (OU um pouco)
^   (XOR um pouco)
~   (NÃO um pouco)
<<  (deslocamento à esquerda)
>>  (deslocamento para a direita)
"""

# Exemplo

x, y = 0b1010, 0b0101 # 10 e 5 em binário
print(bin(x & y))   # 0b0000
print(bin(x | y))   # 0b1111
print(bin(x ^ y))   # 0b1111
print(bin(~x))      # complemento de 1010 -> -0b1011
print(bin(x << 2))  # 0b101000
print(bin(x >> 1))  # 0b0101
