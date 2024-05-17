class Animal():
    especie = ''


class Cachorro(Animal):
    tem_rabo = True
    especie = 'Canis lupus familiaris'
    raca = 'Shitzu'
    nome = 'Paulinho'
    porte = 'Gigante'

    def latir():
        return 'AUAUAUAUAUAUAUAU'

    def comer():
        return 'NhamiNhami'

    def dormir():
        return 'Zzzzzzz...'
    
print(Cachorro.comer())
print(Cachorro.latir())
print(Cachorro.dormir())

