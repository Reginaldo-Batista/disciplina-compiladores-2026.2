diretorios = {
    "Documentos": {
        "Faculdade": {
            "trabalho.py": 15,
            "relatorio.pdf": 250,
            "anotacoes.txt": 30
        },
        "Projetos": {
            "sistema.py": 120,
            "dados.csv": 80
        }
    },
    "Imagens": {
        "foto.png": 500,
        "logo.jpg": 300
    }
}


# Função recursiva
def calcular_tamanho(estrutura):
    total = 0

    for nome, conteudo in estrutura.items():

        if isinstance(conteudo, dict):
            total += calcular_tamanho(conteudo)
        else:
            total += conteudo

    return total


# Função recursiva com callback
def buscar_arquivos(estrutura, criterio, caminho=""):
    encontrados = []

    for nome, conteudo in estrutura.items():
        caminho_atual = f"{caminho}/{nome}"

        if isinstance(conteudo, dict):
            encontrados.extend(
                buscar_arquivos(
                    conteudo,
                    criterio,
                    caminho_atual
                )
            )

        elif criterio(nome):
            encontrados.append(caminho_atual)

    return encontrados


print("=== GERENCIADOR DE ARQUIVOS ===")

tamanho = calcular_tamanho(diretorios)

print(f"Tamanho total: {tamanho} KB")

# Lambda passada como argumento
arquivos_python = buscar_arquivos(
    diretorios,
    lambda nome: nome.endswith(".py")
)

print("\nArquivos Python encontrados:")

for arquivo in arquivos_python:
    print(arquivo)

arquivos_pdf = buscar_arquivos(
    diretorios,
    lambda nome: nome.endswith(".pdf")
)

print("\nArquivos PDF encontrados:")

for arquivo in arquivos_pdf:
    print(arquivo)
