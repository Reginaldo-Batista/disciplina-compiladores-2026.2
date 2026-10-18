# Variável global
total_acessos = 0


def registrar_acesso(usuario):
    global total_acessos

    # Variável local
    mensagem = f"Usuário {usuario} acessou o sistema."

    total_acessos += 1

    print(mensagem)


def criar_contador_sessao():

    # Variável pertencente ao escopo externo
    acessos_sessao = 0

    def contar():
        nonlocal acessos_sessao

        acessos_sessao += 1

        return acessos_sessao

    return contar


sessao_ana = criar_contador_sessao()
sessao_bruno = criar_contador_sessao()

print("=== CONTROLE DE ACESSOS ===")

registrar_acesso("Ana")
registrar_acesso("Bruno")

print("\nAcessos da sessão de Ana:")
print(sessao_ana())
print(sessao_ana())
print(sessao_ana())

print("\nAcessos da sessão de Bruno:")
print(sessao_bruno())

print("\nTotal global de acessos:", total_acessos)