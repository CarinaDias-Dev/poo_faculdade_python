from abc import ABC, abstractmethod
from dataclasses import dataclass


# Classe abstrata veiculo

class Veiculo(ABC):

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def ligar(self):
        pass

# Subclasse Carro

class Carro(Veiculo):
    def mover(self):
        return "O Carro está se movendo."

    def ligar(self):
        return "O carro está ligado."

# Subclasse Bicicleta

class Bicicleta(Veiculo):
    def mover(self):
        return "Bicicleta está se movendo"

    def ligar(self):
        return "Não é possivel ligar uma bicicleta."

#testando as implementações
carro = Carro()
bicicleta = Bicicleta()

print(carro.mover())
print(carro.ligar())
print(bicicleta.mover())
print(bicicleta.ligar())
