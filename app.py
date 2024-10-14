import sqlite3
import os
from tabulate import tabulate # Biblioteca para deixar o menu em uma tabela

class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

class SistemaCadastro:
    def __init__(self):
        # Conexão com o banco de dados
        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()
        # Criação da tabela
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

# Limpa a tela a cada execução
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

# Cadastro de Novos Usuários
    def cadastrar_usuario(self):
        self.limpar_tela()
        nome = input("Nome: ")
        email = input("E-mail: ")
        idade = input("Idade: ")
        usuario = Usuario(nome, email, idade)

        self.cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", 
                            (usuario.nome, usuario.email, usuario.idade))
        self.conn.commit()
        print("Usuário cadastrado com sucesso!")
        input("\nPressione Enter para continuar...")

# Visualização de Usuários Cadastrados
    def visualizar_usuarios(self):
        self.limpar_tela()
        self.cursor.execute("SELECT * FROM usuarios")
        usuarios = self.cursor.fetchall()

        if usuarios:
            tabela = [[usuario[0], usuario[1], usuario[2], usuario[3]] for usuario in usuarios]
            print(tabulate(tabela, headers=["ID", "Nome", "E-mail", "Idade"], tablefmt="fancy_grid"))
        else:
            print("Nenhum usuário cadastrado.")
        input("\nPressione Enter para continuar...")
# Atualização de Usuários
    def atualizar_usuario(self):
        self.limpar_tela()
        id_usuario = input("Digite o ID do usuário que deseja atualizar: ")

        # Verificar se o ID existe no banco de dados
        self.cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
        usuario = self.cursor.fetchone()

# Cria condição para usuário escolher qual campo quer atualizar
        if usuario:
            print(f"\nID: {usuario[0]}, Nome: {usuario[1]}, E-mail: {usuario[2]}, Idade: {usuario[3]}")
            print("\nQual informação você deseja atualizar?")
            opcoes_atualizacao = [
                ["1", "Nome"],
                ["2", "E-mail"],
                ["3", "Idade"]
            ]
            print(tabulate(opcoes_atualizacao, headers=["Opção", "Campo"], tablefmt="fancy_grid"))

            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                novo_nome = input("Novo Nome: ")
                self.cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (novo_nome, id_usuario))
            elif opcao == '2':
                novo_email = input("Novo E-mail: ")
                self.cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (novo_email, id_usuario))
            elif opcao == '3':
                nova_idade = input("Nova Idade: ")
                self.cursor.execute("UPDATE usuarios SET idade = ? WHERE id = ?", (nova_idade, id_usuario))
            else:
                print("Opção inválida.")
                input("\nPressione Enter para continuar...")
                return

            self.conn.commit()

            if self.cursor.rowcount:
                print("Usuário atualizado com sucesso!")
            else:
                print("Erro ao atualizar o usuário.")
        else:
            print("Usuário não encontrado.")
        
        input("\nPressione Enter para continuar...")

# Remoção de Usuários
    def remover_usuario(self):
        self.limpar_tela()
        id_usuario = input("Digite o ID do usuário que deseja remover: ")
        
        # Exibe as informações do usuário antes da confirmação
        self.cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
        usuario = self.cursor.fetchone()

# Condição com menssagem para usuário confirmar ou não a exclusão
        if usuario:
            print(f"\nVocê está prestes a remover o seguinte usuário:")
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, E-mail: {usuario[2]}, Idade: {usuario[3]}")
            confirmacao = input("\nTem certeza que deseja remover este usuário? (s/n): ").lower()

            if confirmacao == 's':
                self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
                self.conn.commit()

                if self.cursor.rowcount:
                    print("Usuário removido com sucesso!")
                else:
                    print("Erro ao remover o usuário.")
            else:
                print("Ação de remoção cancelada.")
        else:
            print("Usuário não encontrado.")
        
        input("\nPressione Enter para continuar...")

# Função que cria Menu e limpa a tela
    def menu(self):
        while True:
            self.limpar_tela()

            # Conteúdo do menu em formato de tabela com traçado contínuo
            opcoes_menu = [
                ["1", "Cadastrar Usuário"],
                ["2", "Visualizar Usuários"],
                ["3", "Atualizar Usuário"],
                ["4", "Remover Usuário"],
                ["5", "Sair"]
            ]

            print(tabulate(opcoes_menu, headers=["Opção", "Descrição"], tablefmt="fancy_grid"))

            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.cadastrar_usuario()
            elif opcao == '2':
                self.visualizar_usuarios()
            elif opcao == '3':
                self.atualizar_usuario()
            elif opcao == '4':
                self.remover_usuario()
            elif opcao == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

    def fechar_conexao(self):
        self.conn.close()

# Executa o sistema
if __name__ == "__main__":
    sistema = SistemaCadastro()
    sistema.menu()
    sistema.fechar_conexao()