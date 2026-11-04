from abstrata.contacliente import ContaCliente


class ContaComum(ContaCliente):
    def __init__(self,numero, IOF, IR, valor_investido, taxa_rendiemnto):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendiemnto)


    def calculo_rendimento(self):
        # Implementação fictícia para calculo de rendimento
        remuneracao =self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF

