from contaclient.conta import Conta
import datetime


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite


    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f'Não existe saldo suficiente na conta número {self.numero}')
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])
            return True

    def depositar(self, valor):
        pass
