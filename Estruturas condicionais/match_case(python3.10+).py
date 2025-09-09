"""
Equivalente a switch em outras linguagens, mas mais poderoso.
Python não tinha switch... mas a partir do Python 3.10 foi introduzido algo muito parecido e até mais poderoso:
Funciona a partir do Python 3.10 ou superior.

- match case é uma estrutura de decisão, permite comparar valores e até desestruturar dados, de forma limpa e clara.

- Quando usar match case?
Quando você tem muitas condições baseadas em um valor;
Quando quer evitar vários if/elif;
Quando quiser deixar o código mais organizado e legível.
"""

# Exemplo 1: menu de operações

op = input("Escolha [+] [-] [*] [/]: ")         # Pede ao usuário para digitar a operação desejada.
a = float(input("a = "))            # 'a' e 'b' pede dois números que serão usados na operação.
b = float(input("b = "))

match op:           # Inicia o bloco de comparação match case. O Python vai comparar o valor de op com os diferentes case abaixo.
    case "+":           # Se o usuário digitou "+", esse bloco é executado.
        print(a + b)
    case "-":           # Se op for "-", o Python faz a subtração a - b.
        print(a - b)
    case "*":           # Se op for "-", o Python faz a subtração a - b.
        print(a * b)
    case "/":                           # Se op for "/", o Python entra neste bloco:
        if b != 0:                      # Primeiro, verifica se b não é zero (b != 0)
            print(a / b)                # Se for diferente de zero → faz a divisão a / b
        else:                           # Se b for zero → exibe a mensagem: "Divisão por zero!", evitando erro.
            print("Divisão por zero!")
    case _:                             # O case _: é o "coriga" (igual ao else ou default).
        print("Operação inválida")      # Ele será executado se nenhuma das opções anteriores for escolhida.


# Exemplo 2: dia da semana

d = int(input("Dia (1–7): "))           # Pede ao usuário para digitar um número de 1 a 7, representando o dia da semana.
match d:                                # Inicia o bloco de match case, que vai comparar o valor da variável d.
    case 1: print("Domingo")            # Se o usuário digitou 1, imprime "Domingo"
    case 2: print("Segunda")            # Cada case verifica se d é igual ao número correspondente.
    case 3: print("Terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sábado")
    case _: print("Valor fora de 1–7")   # O case _: é o curinga. Ele será executado se d não for nenhum dos valores acima.
                                         # Se o usuário digitar 0, 8, 99, etc. Vai mostrar: "Valor fora de 1–7"



