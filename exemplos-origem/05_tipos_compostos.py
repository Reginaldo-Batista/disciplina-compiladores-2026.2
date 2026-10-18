from dataclasses import dataclass
from enum import Enum


# Enumeração
class Situacao(Enum):
    APROVADO = "Aprovado"
    REPROVADO = "Reprovado"


# Registro com diferentes tipos de dados
@dataclass
class Aluno:
    nome: str
    matricula: int
    notas: list


# Lista de objetos
alunos = [
    Aluno("Ana", 101, [8.5, 9.0, 7.5]),
    Aluno("Bruno", 102, [5.0, 6.0, 4.5]),
    Aluno("Carlos", 103, [7.0, 8.0, 9.0])
]

# Tupla
disciplina = ("Programação", "2026.2")

# Conjunto
matriculas = {aluno.matricula for aluno in alunos}

# Dicionário
cadastro = {
    aluno.matricula: aluno
    for aluno in alunos
}


def calcular_media(notas):
    return sum(notas) / len(notas)


print("=== SISTEMA ACADÊMICO ===")
print("Disciplina:", disciplina[0])
print("Período:", disciplina[1])

for aluno in alunos:
    media = calcular_media(aluno.notas)

    situacao = (
        Situacao.APROVADO
        if media >= 7
        else Situacao.REPROVADO
    )

    print(f"\nAluno: {aluno.nome}")
    print(f"Matrícula: {aluno.matricula}")
    print(f"Notas: {aluno.notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao.value}")

print("\nMatrículas cadastradas:", matriculas)

print("Consulta da matrícula 102:")
print(cadastro[102].nome)