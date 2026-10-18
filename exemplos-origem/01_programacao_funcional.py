from functools import reduce

# Lista de produtos vendidos
produtos = [
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Mouse", "preco": 80.00},
    {"nome": "Monitor", "preco": 900.00},
    {"nome": "Mousepad", "preco": 40.00},
    {"nome": "Headset", "preco": 250.00}
]


# Função pura
def aplicar_desconto(preco, percentual):
    return preco * (1 - percentual / 100)


# Função de ordem superior
def processar_produtos(lista, operacao):
    return list(map(operacao, lista))


# Lambda para calcular preços com desconto.
produtos_desconto = processar_produtos(
    produtos,
    lambda produto: {
        "nome": produto["nome"],
        "preco": aplicar_desconto(produto["preco"], 10)
    }
)


# Filter seleciona produtos acima de R$ 100.
produtos_caros = list(
    filter(
        lambda produto: produto["preco"] > 100,
        produtos_desconto
    )
)


# Reduce calcula o faturamento total.
faturamento = reduce(
    lambda total, produto: total + produto["preco"],
    produtos_desconto,
    0
)


print("=== RELATÓRIO DE VENDAS ===")

for produto in produtos_desconto:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

print("\nProdutos acima de R$ 100:")

for produto in produtos_caros:
    print(produto["nome"])

print(f"\nFaturamento total: R$ {faturamento:.2f}")