from banco import Banco
from contacliente import  ContaCliente
from contacomum import ContaComum
from contaremunerada import ContaRemunerada

banco1 = Banco(999, "Teste")
conta_cliente1 = ContaCliente(1, 0.01, 0.1, 1000, 0.05)
conta_comum = ContaComum(2, 0.01, 0.1, 2000, 0.05)
conta_remunerada = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

banco1.adicionar_conta(conta_cliente1)
banco1.adicionar_conta(conta_comum)
banco1.adicionar_conta(conta_remunerada)

banco1.calcular_rendimento_mensal()
banco1.imprime_saldo_contas()