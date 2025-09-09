"""
    Tuplas

Mutabilidade: Imutáveis, impossibilitando alterações após criação. 
Ordenação: Mantêm a ordem dos elementos. 
Indexação: Suporta acesso por índices, como listas. 
Eficiência: Mais folhas em memória que listas.

-> Tuplas: Sequências imutáveis que mantêm a ordem dos elementos.

***Tuplas são criadas com pares (()) ou tuple(). Sua imutabilidade as torna ideais para dados constantes.***

Tuplas: Usadas para configurações fixas, como conexões de banco de dados (host, porta, usuário) ou coordenadas.
"""

# Exemplo 1: Coordenadas geográficas

ponto = (-23.5505, -46.6333)    # Latitude e longitude de São Paulo
latitude, longitude = ponto    # Desempacotamento
print(f"Latitude: {latitude}, Longitude: {longitude}")     # Saída: Latitude: -23.5505, Longitude: -46.6333


# Exemplo 2: Configurações fixas

config = ("localhost", 8080, "admin")
print(config[1])    # Saída: 8080
# config[1] = 9090      # Erro: tuplas são imutáves 