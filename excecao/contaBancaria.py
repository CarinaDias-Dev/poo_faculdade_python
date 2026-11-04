from excecao.saldoinsuficiente import SaldoInsuficiente


class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficiente(self.saldo, valor)
        self.saldo -= valor
        return self.saldo

# Criando uma conta bancária com saldo de R$100
conta = ContaBancaria(100)

try:
    conta.sacar(150) # Tentando sacar um valor maior que o saldo
except SaldoInsuficiente as e:
    print(e)
