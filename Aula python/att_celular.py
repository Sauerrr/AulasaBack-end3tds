class Celular:
    def __init__ (self, marca, ano, modelo, bateria):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.bateria = bateria

    def ligar(self):
        return 'Fazendo ligação'
    
    def despertar(self):
        return "Radar"
    
    def carregar (self):
        if self.modelo == "Iphone":
            return "Horrivel!"
        else:
            return "Melhor que  do iphone."
    
Celular1 = Celular("Apple", 2024, "Iphone 15 pro max", 0)
print(Celular1.carregar())