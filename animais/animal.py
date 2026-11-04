class Animal:
    def __init__(self, nome):
        self.nome = nome


    def falar(self):
        pass


    def mover(self):
        pass
#Subclasse Cachorro que sobrescreve os métodos falar e mover
class Cachorro(Animal):
    def falar(self):
        return "Au!"

    def mover(self):
        return f"{self.nome} está andando."

#Subclasse Gato que sobescreve os

class Gato(Animal):

    def falar(self):
        return "Miau!"

    def mover(self):
        return f"{self.nome} está andando."

class Vaca(Animal):

    def falar(self):
        return "Muu!"

    def mover(self):
        return f"{self.nome} está andando."

class Voador:

    def voar(self):
        return f"{self.nome} está voando."

#Mixin para animal que podem nadar
class Nadador:

    def nadar(self):
        return f"{self.nome} está nadando."


#Subclasse pato que herda de Animal, voador e Nadador
class Pato(Animal, Voador, Nadador):

    def falar(self):
        return "Quack!"

    def andar(self):
        return f"{self.nome} está andando"

    def mover(self):
        return f"{self.andar()}, {self.nadar()} e {self.voar()}"

class Jacare(Animal, Nadador):

    def andar(self):
        return f"{self.nome} está andando"

    def mover(self):
        return f"{self.andar()}, {self.nadar()} e {self.andar()}"

#Função que usa polimorfismo para chamar o método falar

def fazer_som(animal):
    return animal.falar()

#Função que usa polimorfismo para chamar o método mover
def fazer_movimento(animal):
    return animal.mover()

#Instância das classes
cachorro= Cachorro("Lug")
gato = Gato("Floquinho")
vaca = Vaca("Mimosa")
pato = Pato("Duck")
jacare = Jacare("Felix")

#Chamando os métodos polimórficos
print(fazer_som(cachorro))
print(fazer_som(gato))
print(fazer_som(vaca))
print(fazer_som(pato))


print()
print(fazer_movimento(cachorro))
print(fazer_movimento(gato))
print(fazer_movimento(vaca))
print(fazer_movimento(pato))
print(fazer_movimento(jacare))
