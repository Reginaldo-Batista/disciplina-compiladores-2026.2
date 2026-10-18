# Base de fatos: disciplinas concluídas.
historico = {
    "Ana": {"Algoritmos", "Matematica"},
    "Bruno": {"Algoritmos"},
    "Carlos": {"Algoritmos", "Matematica", "Banco de Dados"}
}


# Regras: pré-requisitos das disciplinas.
pre_requisitos = {
    "Estrutura de Dados": {"Algoritmos"},
    "Banco de Dados": {"Algoritmos"},
    "Inteligencia Artificial": {
        "Estrutura de Dados",
        "Matematica"
    },
    "Projeto de Software": {
        "Banco de Dados"
    }
}


# Consulta lógica
def pode_cursar(aluno, disciplina):
    concluidas = historico.get(aluno, set())
    requisitos = pre_requisitos.get(disciplina)

    if requisitos is None:
        return False

    return requisitos.issubset(concluidas)


# Inferência
def disciplinas_disponiveis(aluno):
    concluidas = historico.get(aluno, set())

    return [
        disciplina
        for disciplina in pre_requisitos
        if disciplina not in concluidas
        and pode_cursar(aluno, disciplina)
    ]


print("=== SISTEMA ACADÊMICO ===")

for aluno in historico:
    print(f"\nEstudante: {aluno}")

    disponiveis = disciplinas_disponiveis(aluno)

    if disponiveis:
        for disciplina in disponiveis:
            print(f"Pode cursar: {disciplina}")
    else:
        print("Nenhuma disciplina disponível.")

print("\n=== CONSULTA ESPECÍFICA ===")

resultado = pode_cursar("Ana", "Banco de Dados")

print(f"Ana pode cursar Banco de Dados? {resultado}")