import datetime
from extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return "Saldo insuficiente!"
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque", valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não existe saldo sufiente"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["Tranferencia", valor, "Data", datetime.datetime.today()])
            return "Transferência Realizada"

    def gerarsaldo(self):
        print(f"Numero: {self.numero}\nSaldo: {self.saldo}")
        print(f"Saldo: R${self.saldo:10.2f}")
