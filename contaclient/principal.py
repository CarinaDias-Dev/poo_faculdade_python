from cliente import Cliente
from conta import Conta
from contaEspecial import ContaEspecial

#As três contas foram iniciadas, as contas comuns com saldo 2000 e a contaEspecial 1000
cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")
cliente3 = Cliente("789", "Joana", "Rua H")

#As três contas foram iniciadas, as contas comuns com saldo 2000 e a conta
conta1 = Conta(cliente2, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 1000, 2000)

#Impresso o saldo das três contas
print(f"Cliente: {cliente1.cpf} da conta comum {conta1.numero} possui saldo {conta1.saldo}")
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo {conta2.saldo}")
print(f"Cliente: {cliente3.cpf} da conta comum {conta3.numero} possui saldo {conta3.saldo} e limite de {conta3.limite}")

#Depositou 500 e tentou sacar 3000 da conta comum que não terá saldo
conta2.depositar(500)
print("\nSaldo após depósito de R$500 conta2")
#Mensagem indicando saldo após depósito
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo {conta2.saldo}")

conta2.sacar(3000)
#mensagem indicando saldo após saque
print("\nSaldo após saque de R$3000.")
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo de {conta2.saldo}")

#Depositou 100 e tentou sacar 2000 da conta especial que tem imite
conta3.depositar(100)
#Mensagem indicando saldo após deposito
print("\nSaldo Após depósitar R$100 cliente especial.")
print(f"Cliente: {cliente3.cpf} da conta Especial {conta3.numero} possui saldo de {conta3.saldo} e limite de {conta3.limite}")
conta3.sacar(2000)
#Mensagem indicando saldo após saque
print("\nSaldo após saque de R$2000 cliente especial")
print(f"Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo de {conta3.saldo} e limite de {conta3.limite}")
