from abc import ABC, abstractmethod


# Classe abstrata
class ContaBancaria(ABC):

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O depósito deve ser positivo.")

        self.__saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def _retirar(self, valor):
        self.__saldo -= valor

    def exibir_saldo(self):
        print(f"{self.titular}: R$ {self.saldo:.2f}")


# Herança
class ContaCorrente(ContaBancaria):

    def sacar(self, valor):
        if valor <= 0:
            return False

        if valor <= self.saldo + 500:
            self._retirar(valor)
            return True

        return False


class ContaPoupanca(ContaBancaria):

    def sacar(self, valor):
        if valor <= 0:
            return False

        if valor <= self.saldo:
            self._retirar(valor)
            return True

        return False


# Polimorfismo
def realizar_saque(conta, valor):
    if conta.sacar(valor):
        print("Saque realizado com sucesso!")
    else:
        print("Saque não autorizado.")


# Criação dos objetos
conta1 = ContaCorrente("Ana", 1000)
conta2 = ContaPoupanca("Bruno", 1000)

print("=== SISTEMA BANCÁRIO ===")

realizar_saque(conta1, 1200)
realizar_saque(conta2, 1200)

conta1.exibir_saldo()
conta2.exibir_saldo()