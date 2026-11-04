class Extrato:

    def __init__(self):
        self.transacoes = []

    def gerar_extrato(self, conta):
        print(f'Extrato da conta {conta}')
        for transacoes in self.transacoes:
            print(f"{transacoes[0]:15s}, {transacoes[1]} {transacoes[2]} {transacoes[3]}")