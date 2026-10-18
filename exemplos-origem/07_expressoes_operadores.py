preco_unitario = 120
quantidade = 3
cliente_vip = True
cupom_valido = False

# Expressão aritmética
subtotal = preco_unitario * quantidade

# Expressão relacional
compra_alta = subtotal >= 300

# Expressão lógica
recebe_desconto = cliente_vip and compra_alta

# Expressão condicional
percentual = 0.15 if recebe_desconto else 0.05

# Atribuição composta
desconto = subtotal * percentual
total = subtotal
total -= desconto

# Precedência dos operadores
resultado_sem_parenteses = 10 + 5 * 2
resultado_com_parenteses = (10 + 5) * 2

# Curto-circuito lógico
def verificar_cupom():
    print("Consultando cupom...")
    return cupom_valido


cupom_aplicavel = False and verificar_cupom()

# Operação bit a bit
permissoes = 0b1010
permissao_consulta = 0b0010

tem_permissao = bool(
    permissoes & permissao_consulta
)

print("=== RESUMO DA COMPRA ===")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")

print("\n=== EXPRESSÕES ===")
print("Sem parênteses:", resultado_sem_parenteses)
print("Com parênteses:", resultado_com_parenteses)
print("Cupom aplicável:", cupom_aplicavel)
print("Permissão de consulta:", tem_permissao)