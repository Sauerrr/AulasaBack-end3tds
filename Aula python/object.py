class person:
    def __init__(self, altura, nome, cor, idade):
        self.altura = altura
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def __str__(self):
        return f'nome: {self.nome}, altura: {self.altura}, cor: {self.cor}'
    


people = person(1.30, 'maria do buraco', 'branca', 15)

print(people)


