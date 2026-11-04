#Herança Multipla
from contaclient import conta, poupanca
from contaclient.conta import Conta
from contaclient.poupanca import Poupanca

class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __int__(self, taxa_remuneracao, clientes, numero, saldo):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)


    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracaoMes / 30)