"""
Você pode colocar um if dentro de outro para cenários ainda mais específicos.

Dica: muitos níveis de aninhamento podem dificultar a manutenção. Considerar funções
para esclarecer a lógica.

- "Muitos níveis de aninhamento" 
Significa ter vários blocos dentro de blocos.
Isso torna o código difícil de entender, testar e corrigir, especialmente se você tiver muitos if, for ou while uns dentro dos outros.

- "Podem dificultar a manutenção"
Manutenção = entender, corrigir, adaptar ou melhorar o código no futuro.
Quando o código está muito "profundo", fica confuso e fácil de errar.

- "Considerar funções para esclarecer a lógica"
Em vez de deixar tudo em um único bloco, divida a lógica em funções com nomes claros.
"""

# Exemplo: login e senha

usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin":
    if senha == "1234":
        print("Acesso liberado!")
    else:
        print("Senha incorreta!")
else:  
    print("Usuário não encontrado!")   

