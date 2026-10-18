# Exceções personalizadas
class SaldoInsuficienteError(Exception):
    pass


class ContaInexistenteError(Exception):
    pass


class ValorInvalidoError(Exception):
    pass


contas = {
    101: {"titular": "Ana", "saldo": 1500},
    102: {"titular": "Bruno", "saldo": 800},
    103: {"titular": "Carlos", "saldo": 200}
}


def transferir(origem, destino, valor):

    # Verificação das contas
    if origem not in contas:
        raise ContaInexistenteError(
            "Conta de origem inexistente."
        )

    if destino not in contas:
        raise ContaInexistenteError(
            "Conta de destino inexistente."
        )

    # Verificação do valor
    if valor <= 0:
        raise ValorInvalidoError(
            "O valor deve ser maior que zero."
        )

    # Verificação do saldo
    if contas[origem]["saldo"] < valor:
        raise SaldoInsuficienteError(
            "Saldo insuficiente para transferência."
        )

    # Transferência
    contas[origem]["saldo"] -= valor
    contas[destino]["saldo"] += valor

    return True


def realizar_operacao(origem, destino, valor):

    try:
        print(f"\nTransferindo R$ {valor:.2f}")

        transferir(origem, destino, valor)

    except SaldoInsuficienteError as erro:
        print("Erro financeiro:", erro)

    except ContaInexistenteError as erro:
        print("Erro cadastral:", erro)

    except ValorInvalidoError as erro:
        print("Erro de validação:", erro)

    else:
        print("Transferência realizada com sucesso!")

    finally:
        print("Operação encerrada.")


print("=== SISTEMA DE TRANSFERÊNCIAS ===")

realizar_operacao(101, 102, 300)

realizar_operacao(103, 102, 1000)

realizar_operacao(999, 101, 100)

realizar_operacao(101, 102, -50)

print("\n=== SALDOS FINAIS ===")

for numero, conta in contas.items():
    print(
        f"Conta {numero} - {conta['titular']}: "
        f"R$ {conta['saldo']:.2f}"
    )