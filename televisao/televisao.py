class Televisao:
    def __init__(self, pcanal, max, min):
        self.canal = pcanal
        self.cmin = min
        self.cmax = max


    def muda_canal_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin


tv1 = Televisao(2, 2, 10)
print(f"Canal Sintonizado: {tv1.canal}")
print(f"Mudando canal para cima")
for x in range(1, 20):
    tv1.muda_canal_cima()
    print(f"Canal sintonizado: {tv1.canal}")

tv2 = Televisao(10, 2, 10)
print(f"Canal sintonizado: {tv2.canal}")
print("Mudando canal para baioxo")
for x in range(1, 20):
    tv2.muda_canal_baixo()
    print(f"Canal sintonizado: {tv2.canal}")
