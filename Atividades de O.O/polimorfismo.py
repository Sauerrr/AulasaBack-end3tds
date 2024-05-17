class Animal:
    def emitir_som(self):
        return "Qualquer som"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "AUAUAUAUAUAUAUAUAU"
    
cachorro = Cachorro()
print(cachorro.emitir_som())

class Gato(Animal):
    def emitir_som(self):
        return 'Miau'