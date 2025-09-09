"""
Exemplos de Condições Compostas

São condições que combinam duas ou mais expressões lógicas usando operadores lógicos como:

and (e)
or (ou)
not (não)

Essas condições permitem que você teste mais de uma coisa ao mesmo tempo em um if.
"""

# 1. Divisível por 3 e 5

n = int(input("Digite um número: "))
if n % 3 == 0 and n % 5 == 0:           # Verifica se n é divisível por 3 e por 5 ao mesmo tempo
    print("Divisível por 3 e 5")        # n % 3 → calcula o resto da divisão de n por 3 - n % 5 → calcula o resto da divisão de n por 5
                                        # Quando o resto é 0, significa que o número é divisível.
                                        # and → só retorna True se as duas condições forem verdadeiras.


# 2. Ano bissexto

ano = int(input("Ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):           # Um ano é bissexto se for:
    print("Ano bissexto")                                           # Divisível por 4 e ao mesmo tempo
else:                                                               # Não divisível por 100 OU 
    print("Ano comum")                                              # O ano também é bissexto se for: Divisível por 400


# 3. Lados de um triângulo

a, b, c = map(int, input("Lados a b c: ").split())            # input("Lados a b c: ") → pede que o usuário digite 3 valores separados por espaço.
if a + b > c and a + c > b and b + c > a:                     # .split() → separa esses valores em uma lista de strings: ['3', '4', '5']
    print("Triângulo válido")                                 # map(int, ...) → converte cada item da lista para inteiro.
else:                                                         # a + b > c  -> A soma dos lados a e b precisa ser maior que o lado c.
    print("Não é triângulo")                                  # a + c > b  -> A soma de a com c precisa ser maior que o lado b.
                                                              # b + c > a  -> A soma de b com c precisa ser maior que o lado a.





