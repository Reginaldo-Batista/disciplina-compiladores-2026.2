import re
from dataclasses import dataclass
from functools import reduce


# Registro de dados
@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int


# Classe com encapsulamento
class Loja:

    def __init__(self):
        self.__produtos = {}
        self.__eventos = []

    def cadastrar_produto(self, codigo, produto):
        self.__produtos[codigo] = produto

    def registrar_evento(self, funcao):
        self.__eventos.append(funcao)

    def emitir_evento(self, mensagem):
        for funcao in self.__eventos:
            funcao(mensagem)

    def consultar_produto(self, codigo):
        return self.__produtos.get(codigo)

    def realizar_compra(self, codigo, quantidade):

        produto = self.consultar_produto(codigo)

        if produto is None:
            raise ValueError("Produto inexistente.")

        if quantidade <= 0:
            raise ValueError("Quantidade inválida.")

        if quantidade > produto.estoque:
            raise ValueError("Estoque insuficiente.")

        subtotal = produto.preco * quantidade

        desconto = calcular_desconto(subtotal)

        total = subtotal - desconto

        produto.estoque -= quantidade

        self.emitir_evento(
            f"Venda realizada: {produto.nome}"
        )

        return total


# Função pura
def calcular_desconto(valor):
    percentual = 0.10 if valor >= 500 else 0.05

    return valor * percentual


# Expressão regular
def validar_codigo(codigo):
    return bool(
        re.fullmatch(r"PROD-\d{3}", codigo)
    )


# Callback
def notificar_venda(mensagem):
    print("NOTIFICAÇÃO:", mensagem)


# Criação do sistema
loja = Loja()

loja.registrar_evento(notificar_venda)


# Cadastro dos produtos
loja.cadastrar_produto(
    "PROD-001",
    Produto("Teclado", 150, 10)
)

loja.cadastrar_produto(
    "PROD-002",
    Produto("Monitor", 900, 5)
)

loja.cadastrar_produto(
    "PROD-003",
    Produto("Mouse", 80, 20)
)


# Lista de pedidos
pedidos = [
    ("PROD-001", 2),
    ("PROD-002", 1),
    ("PROD-003", 3)
]


valores_vendas = []

print("=== SISTEMA INTEGRADOR ===")


for codigo, quantidade in pedidos:

    try:

        if not validar_codigo(codigo):
            raise ValueError("Código inválido.")

        total = loja.realizar_compra(
            codigo,
            quantidade
        )

        valores_vendas.append(total)

        print(
            f"Pedido {codigo}: R$ {total:.2f}"
        )

    except ValueError as erro:
        print("Erro:", erro)


# Programação funcional
faturamento = reduce(
    lambda acumulado, valor: acumulado + valor,
    valores_vendas,
    0
)


print("\n=== RELATÓRIO FINAL ===")

print(f"Faturamento: R$ {faturamento:.2f}")

print("Pedidos processados:", len(valores_vendas))