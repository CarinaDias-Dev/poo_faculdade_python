class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def depositar(self, valor):
        self.saldo += valor

    def gerar_extrato(self):
        print(f"Numero: {self.numero} \nCPF: {self.cpf} \nSaldo: {self.saldo}")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não existe saldo o suficiente"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return "Transferência Realizada."

#Instânciar a classe
c1 = Conta(1, 123, "João", 0)
c2 = Conta(3, 456, 'Carina', 0)
c1.depositar(1000)
c1.sacar(100)
c1.gerar_extrato()
c1.transfereValor(c2, 500)


print(c1.saldo)