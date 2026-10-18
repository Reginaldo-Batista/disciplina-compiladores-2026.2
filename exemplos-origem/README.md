# Exemplos em Python

Esta pasta contém 15 programas independentes escritos escritos na linguagem de origem: Python.

## Requisitos

- Python 3.10 ou superior.
- Nenhuma biblioteca externa é necessária; todos os exemplos usam apenas a biblioteca padrão do Python.

O interpretador utilizado é o [CPython](https://www.python.org/), a implementação de referência da linguagem Python.

## Instalação do Python

### Linux

Em distribuições Debian, Ubuntu e derivadas:

```bash
sudo apt update
sudo apt install python3
```

Em distribuições Fedora:

```bash
sudo dnf install python3
```

### macOS

Com o Homebrew:

```bash
brew install python
```

Ou baixe o instalador do CPython em [python.org/downloads](https://www.python.org/downloads/).

### Windows

Baixe e execute o instalador do CPython em [python.org/downloads](https://www.python.org/downloads/). Durante a instalação, selecione a opção **Add Python to PATH**.

## Verificar a instalação

No terminal, execute um dos comandos abaixo:

```bash
python3 --version
```

Ou, alternativamente:

```bash
python --version
```

A versão informada deve ser 3.10 ou superior.

## Executar os exemplos

A partir da raiz do repositório, execute qualquer arquivo com:

```bash
python3 exemplos-origem/01_programacao_funcional.py
```

No Windows, quando `python3` não estiver disponível, use:

```powershell
python exemplos-origem\01_programacao_funcional.py
```

Também é possível entrar nesta pasta e executar um arquivo diretamente:

```bash
python3 15_sistema_integrador.py
```

Cada programa pode ser executado de forma isolada. O arquivo `08_fluxos_controle.py` é interativo: informe as opções solicitadas no terminal até finalizar o pedido.
