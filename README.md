#  CadPy - Sistema de Cadastro de Usuários

Este projeto é um sistema de cadastro de usuários feito em Python com SQLite. Ele permite a criação, visualização, atualização e remoção de usuários, com persistência de dados entre as execuções do programa.

## Funcionalidades

- **Cadastrar Usuário**: Insere novos usuários no banco de dados, informando nome, e-mail e idade.
- **Visualizar Usuários**: Exibe uma tabela com todos os usuários cadastrados.
- **Atualizar Usuário**: Permite editar as informações de um usuário já cadastrado.
- **Remover Usuário**: Remove um usuário do banco de dados após confirmação.
- **Persistência de Dados**: Os dados são armazenados em um banco de dados SQLite, permitindo o uso contínuo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **SQLite**: Banco de dados relacional.
- **Tabulate**: Biblioteca para exibição de dados em formato de tabela no terminal.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado em seu sistema.
- Bibliotecas necessárias listadas no arquivo `requirements.txt`.

### Instalação das dependências

1. Clone o repositório ou baixe o código-fonte.

git clone https://github.com/paulocastanha33/cadpy.git
cd cadpy

2. Instale as dependências necessárias executando o seguinte comando no terminal:

pip3 install -r requirements.txt

# Exemplo de Uso

    Ao iniciar o sistema, o menu exibido será semelhante a este:

+--------+---------------------+
| Opção  | Descrição           |
+--------+---------------------+
| 1      | Cadastrar Usuário   |
| 2      | Visualizar Usuários |
| 3      | Atualizar Usuário   |
| 4      | Remover Usuário     |
| 5      | Sair                |
+--------+---------------------+

Escolha uma opção digitando o número correspondente.

# Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie um branch para sua feature ou correção e envie um pull request.
Licença

Este projeto está licenciado sob a MIT License.

