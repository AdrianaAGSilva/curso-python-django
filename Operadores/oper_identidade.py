"""
Compare se duas variáveis referenciam o mesmo objeto na memória.

is
is not
"""

# Exemplo

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (mesma referência)
print(a is c)   # False (objetos diferentes, apesar de iguais)  