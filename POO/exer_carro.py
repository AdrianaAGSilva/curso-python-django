class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 # não está como parâmetro de entrada

    def acelerar(self, incremento):
        self.velocidade += incremento
        return self.velocidade

    def desacelerar(self, decremento):
        return self.velocidade

    def exibir_infor(self):
        print(f"Carro: {self.marca} {self.modelo} {self.ano}")
        print(f"Velocidade: {self.velocidade}")  

a = Carro("VolksWagem", "Gol", 2007)       
a.exibir_infor()
a.acelerar(20)
a.acelerar(40)
a.desacelerar(10)
a.exibir_infor()

b = Carro("VolksWagem", "Jetta", 2018)
b.exibir_infor()

c = Carro("Fiat", "Argo", 2020)
c.exibir_infor()
    
    
 

