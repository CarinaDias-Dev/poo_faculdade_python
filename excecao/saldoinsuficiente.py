class SaldoInsuficiente(Exception):
    def __init__(self, saldo, valor_saque):
        mensagem = f"Saldo insuficiente. Saldo atual: {saldo}, valor do saque: {valor_saque}"
        super().__init__(mensagem)
        self.saldo = saldo
        self.valor_saque = valor_saque

    def __str__(self):
        return f"Saldo insuficiente: {self.args[0]}"