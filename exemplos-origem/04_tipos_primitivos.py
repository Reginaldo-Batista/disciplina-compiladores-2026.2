from decimal import Decimal

# Dados de um produto
nome = "Notebook"
quantidade = 5
preco = Decimal("3499.90")
disponivel = True
codigo = "1025"

# Conversão explícita de string para inteiro
codigo_numerico = int(codigo)

# Conversão de inteiro para string
identificador = "PROD-" + str(codigo_numerico)

# Cálculo utilizando Decimal para valores monetários
valor_estoque = preco * quantidade

# Operação lógica
pode_vender = disponivel and quantidade > 0

# Exemplo de número complexo
impedancia = 3 + 4j

print("=== CADASTRO DE PRODUTO ===")
print("Produto:", nome)
print("Identificador:", identificador)
print("Quantidade:", quantidade)
print("Preço: R$", preco)
print("Valor do estoque: R$", valor_estoque)
print("Disponível para venda:", pode_vender)

print("\n=== TIPOS DE DADOS ===")
print("Nome:", type(nome))
print("Quantidade:", type(quantidade))
print("Preço:", type(preco))
print("Disponibilidade:", type(disponivel))
print("Código:", type(codigo_numerico))

print("\n=== NÚMERO COMPLEXO ===")
print("Impedância:", impedancia)
print("Parte real:", impedancia.real)
print("Parte imaginária:", impedancia.imag)