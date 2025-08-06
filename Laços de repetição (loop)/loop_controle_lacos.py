"""
É o uso de comandos especiais dentro de loops (for ou while) para:

break: Interrompe o laço imediatamente. (interromper)

continue: Pula para a próxima iteração, ignorando o restante do bloco atual. (pular)

else: Executado quando o laço termina normalmente (sem break). (alterar o fluxo da repetição)
"""

# Exemplo com 'break' e 'continue'

numeros = [1, 2, 3, 4, 5, 6]        # Cria uma lista com os números de 1 a 6.
for num in numeros:             # Inicia um laço for, onde num vai percorrer cada valor da lista: 1, 2, 3, 4...
    if num == 4:        # Se o número atual for 4, imprime uma mensagem e interrompe o laço com break.
        print("Encontramos o 4, parando o laço!")        # nada mais será executado depois disso, mesmo que a lista continue com mais números.
        break
    if num % 2 == 0:            # Se o número for par (ou seja, resto da divisão por 2 for 0), pula o restante do laço e volta pro próximo número.
        continue                # Ou seja, não imprime o número par — ele é ignorado.
    print(f"Número ímpar: {num}")           # Só chega aqui se o número não for 4 e não for par → ou seja, apenas para os números ímpares diferentes de 4.


# Exemplo com else

numeros_par = [1, 3, 5, 7]      # Cria uma lista apenas com números ímpares.
for nume in numeros_par:        # Percorre a lista, um número por vez.
    if nume % 2 == 0:        # Verifica se o número atual é par (resto da divisão por 2 igual a 0).  
        print("Encontramos um número par!")         # Como todos os números da lista são ímpares, essa condição nunca será verdadeira.
        break           # Se encontrasse um número par, pararia imediatamente o laço.
else:           # Esse else está ligado ao for, não ao if. Ele só será executado se o for terminar normalmente, ou seja, sem cair no break.
    print("Nenhum número par encontrado.")         # Como nenhum número par foi encontrado, o laço for termina normalmente, e essa mensagem é exibida.
    

# Dica extra:
# O 'else' com 'for' é útil quando você está procurando algo e quer saber se não encontrou.