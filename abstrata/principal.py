from abstrata.contacomum import ContaComum
from abstrata.contavip import ContaVip

cc1 = ContaComum(1, 0.1, 0.25, 2000, 0.05)
cv1 = ContaVip(2, 0.1, 0.25,2000, 0.05)

cc1.calculo_rendimento()
cv1.calculo_rendimento()

cc1.extrato()
cv1.extrato()
