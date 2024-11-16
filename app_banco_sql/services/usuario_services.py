from app_banco_sql.models.usuario_model import Usuario
from app_banco_sql.repositores.usuario_repositore import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuario ja cadastrado!")
                return
                
            self.repository.salvar_usuario(usuario)
            print("Usuario cadastrado com sucesso!")

        except TypeError as erro:
            print(f"Erro ao salvar o usuario: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
    
    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
    
    def pesquisar_unico_usuario(self):
        try:
            pesquisar_email = input("Digite o email desejado: ")
            cadastroEmail = self.repository.pesquisar_usuario_por_email(email=pesquisar_email)

            if cadastroEmail:
                print(f"nome: {cadastroEmail.nome} | email: {cadastroEmail.email} | senha: {cadastroEmail.senha}")
                return
            else:
                print("Usuario não consta no banco de dados.")
                return
        except TypeError as error:
            print(f"Erro ao pesquisar o usuario: {error}")
        except Exception as error:
            print(f"Erro inesperado: {error}")
    
    def atualizar_dados_usuario(self):
        try:
            pesquisar_email = input("Digite o email desejado: ")
            cadastroEmail = self.repository.pesquisar_usuario_por_email(email=pesquisar_email)

            if cadastroEmail:
                cadastroEmail.nome = input("Digite um novo nome para o usuario: ")
                cadastroEmail.email = input("Digite um novo email para o usuario: ")
                cadastroEmail.senha = input("Digite uma nova senha para o usuario: ")
                self.repository.atualizar_usuario(cadastroEmail)
                print("\nDados Atualizados com sucesso.")
            else:
                print("Usuario não consta no banco de dados.")
                return
        
        except TypeError as error:
            print(f"Erro ao atualizador dados de usuario: {error}")
        except Exception as error:
            print(f"Erro inesperado: {error}")
        
    def excluir_dados_usuario(self):
        try:
            pesquisar_email = input("Digite o email desejado: ")
            cadastroEmail = self.repository.pesquisar_usuario_por_email(email=pesquisar_email)

            if cadastroEmail:
                self.repository.excluir_usuario(cadastroEmail)
                print("Usuario excluido do banco de dados com sucesso.")
            else:
                print("Usuario não consta no banco de dados.")
                return
        
        except TypeError as error:
            print(f"Erro ao excluir o usuario: {error}")
        except Exception as error:
            print(f"Erro inesperado: {error}")