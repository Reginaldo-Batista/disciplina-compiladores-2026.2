# Função com parâmetros posicionais e opcionais
def calcular_salario(salario_base, horas_extras=0, valor_hora=20):
    adicional = horas_extras * valor_hora
    return salario_base + adicional


# Função com quantidade variável de argumentos
def calcular_bonus(*valores):
    return sum(valores)


# Função com argumentos nomeados variáveis
def cadastrar_funcionario(**dados):
    print("\n=== DADOS DO FUNCIONÁRIO ===")

    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


# Função com retorno de múltiplos valores
def calcular_pagamento(salario_bruto):
    desconto = salario_bruto * 0.08
    salario_liquido = salario_bruto - desconto

    return desconto, salario_liquido


# Demonstração de referências a objetos mutáveis
def adicionar_beneficio(beneficios, novo_beneficio):
    beneficios.append(novo_beneficio)


def tentar_alterar_salario(salario):
    salario = 10000
    return salario


print("=== SISTEMA DE FOLHA DE PAGAMENTO ===")

# Argumentos posicionais
salario_ana = calcular_salario(2500, 10, 25)

# Argumentos nomeados
salario_bruno = calcular_salario(
    salario_base=3000,
    valor_hora=30,
    horas_extras=5
)

bonus = calcular_bonus(100, 150, 200)

salario_ana += bonus

desconto, salario_liquido = calcular_pagamento(salario_ana)

cadastrar_funcionario(
    nome="Ana",
    cargo="Analista",
    salario=salario_ana,
    setor="Tecnologia"
)

beneficios = ["Vale-transporte"]

adicionar_beneficio(beneficios, "Vale-alimentação")

print("\n=== RESULTADOS ===")
print(f"Salário bruto de Ana: R$ {salario_ana:.2f}")
print(f"Salário de Bruno: R$ {salario_bruno:.2f}")
print(f"Desconto de Ana: R$ {desconto:.2f}")
print(f"Salário líquido de Ana: R$ {salario_liquido:.2f}")

print("\nBenefícios:", beneficios)

novo_valor = tentar_alterar_salario(salario_ana)

print("Valor retornado pela função:", novo_valor)
print("Salário original:", salario_ana)