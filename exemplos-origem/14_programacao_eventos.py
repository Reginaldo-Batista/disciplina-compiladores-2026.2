class GerenciadorEventos:

    def __init__(self):
        self.eventos = {}

    def registrar(self, evento, funcao):

        if evento not in self.eventos:
            self.eventos[evento] = []

        self.eventos[evento].append(funcao)

    def disparar(self, evento, dados):

        if evento in self.eventos:

            for funcao in self.eventos[evento]:
                funcao(dados)


# Funções que respondem aos eventos
def enviar_email(pedido):
    print(
        f"E-mail enviado para {pedido['cliente']}."
    )


def atualizar_estoque(pedido):
    print(
        f"Estoque atualizado: "
        f"{pedido['quantidade']} unidade(s) vendida(s)."
    )


def registrar_venda(pedido):
    print(
        f"Venda registrada no valor de "
        f"R$ {pedido['valor']:.2f}"
    )


# Criação do gerenciador
gerenciador = GerenciadorEventos()

# Registro dos ouvintes
gerenciador.registrar("pedido_realizado", enviar_email)

gerenciador.registrar("pedido_realizado", atualizar_estoque)

gerenciador.registrar("pedido_realizado", registrar_venda)


# Simulação de um pedido
pedido = {
    "cliente": "Ana",
    "produto": "Notebook",
    "quantidade": 1,
    "valor": 3500
}


print("=== SISTEMA DE PEDIDOS ===")

print("Novo pedido recebido!")

gerenciador.disparar("pedido_realizado", pedido)

print("\nProcessamento concluído.")