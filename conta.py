class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria("Marcos", 100)

print("Titular:", conta.titular)
print("Saldo:", conta.consultar_saldo())

conta.depositar(50)
print("Saldo:", conta.consultar_saldo())

conta.sacar(30)
print("Saldo:", conta.consultar_saldo())

conta.sacar(1000)
print("Saldo:", conta.consultar_saldo())