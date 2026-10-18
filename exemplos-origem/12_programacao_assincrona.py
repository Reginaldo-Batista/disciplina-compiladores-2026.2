import asyncio
import time


# Simula uma consulta a um fornecedor
async def consultar_fornecedor(nome, tempo, quantidade):

    print(f"Iniciando consulta: {nome}")

    # Simula uma operação de entrada e saída
    await asyncio.sleep(tempo)

    print(f"Consulta finalizada: {nome}")

    return {
        "fornecedor": nome,
        "quantidade": quantidade
    }


async def main():

    print("=== CONSULTA DE ESTOQUES ===")

    inicio = time.perf_counter()

    # Executa as consultas concorrentemente
    resultados = await asyncio.gather(
        consultar_fornecedor("Fornecedor A", 3, 50),
        consultar_fornecedor("Fornecedor B", 2, 30),
        consultar_fornecedor("Fornecedor C", 1, 80)
    )

    fim = time.perf_counter()

    total_produtos = sum(
        resultado["quantidade"]
        for resultado in resultados
    )

    print("\n=== RESULTADOS ===")

    for resultado in resultados:
        print(
            f"{resultado['fornecedor']}: "
            f"{resultado['quantidade']} unidades"
        )

    print(f"\nEstoque total: {total_produtos}")

    print(
        f"Tempo de execução: {fim - inicio:.2f} segundos"
    )


asyncio.run(main())