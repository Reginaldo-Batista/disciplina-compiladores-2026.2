cardapio = {
    1: ("Hambúrguer", 18.00),
    2: ("Pizza", 35.00),
    3: ("Refrigerante", 7.00),
    4: ("Batata frita", 12.00)
}

carrinho = []

print("=== LANCHONETE PYTHON ===")

while True:

    print("\n1 - Ver cardápio")
    print("2 - Adicionar produto")
    print("3 - Consultar carrinho")
    print("4 - Finalizar pedido")

    opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":
            print("\n=== CARDÁPIO ===")

            for codigo, produto in cardapio.items():
                nome, preco = produto

                print(f"{codigo} - {nome}: R$ {preco:.2f}")

        case "2":
            try:
                codigo = int(input("Código do produto: "))
            except ValueError:
                print("Digite um código numérico.")
                continue

            if codigo not in cardapio:
                print("Produto não encontrado.")
                continue

            carrinho.append(cardapio[codigo])

            print("Produto adicionado!")

        case "3":
            if not carrinho:
                print("Carrinho vazio.")
                continue

            total = 0

            for nome, preco in carrinho:
                print(f"{nome}: R$ {preco:.2f}")
                total += preco

            print(f"Total: R$ {total:.2f}")

        case "4":
            if not carrinho:
                print("Adicione produtos antes de finalizar.")
                continue

            total = sum(
                preco for nome, preco in carrinho
            )

            if total >= 100:
                desconto = total * 0.10
            elif total >= 50:
                desconto = total * 0.05
            else:
                desconto = 0

            total_final = total - desconto

            print(f"\nTotal final: R$ {total_final:.2f}")
            print("Pedido finalizado!")

            break

        case _:
            print("Opção inválida.")