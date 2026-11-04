import datetime


class Poupanca:
    def __init__(self, taxa_remuneracao):
        self.taxaremuneracaoMes =taxa_remuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneracao(self):   #Aplica a remuneração da conta
        self.saldo += self.saldo * self.taxaremuneracaoMes