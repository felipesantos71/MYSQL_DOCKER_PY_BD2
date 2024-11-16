import os
import sys

#Adiciona o diretório 'app' como diretório padrão
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app_banco_sql.services.usuario_services import UsuarioService
from app_banco_sql.repositores.usuario_repositore import UsuarioRepository
from app_banco_sql.config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuario
    while True:
        #Opcoes do sistema
        print("\nOpções do Banco")
        print("1- Adicionar um usuário.")
        print("2- Pesquisar um usuário.")
        print("3- Atualizar dados de um usuário.")
        print("4- Excluir um usuário.")
        print("5- Listar todos os usuários.")
        print("0- Sair da aplicação.")

        resposta = input("Informe a opção desejada!")
        os.system("cls || clear")

        match(resposta):
            case 1:        
                print("Cadastrando novo usuário.")
                novoNome = input("Digite seu nome: ")
                novoEmail = input("Digite seu email: ")
                novaSenha = input("Digite seu senha: ")

                service.criar_usuario(nome=novoNome,email=novoEmail,senha=novaSenha)
            case 2:
                service.pesquisar_unico_usuario()
            case 3:
                service.atualizar_dados_usuario()
            case 4:
                service.excluir_dados_usuario()
            case 5:
                print("\nListando usuarios cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
            case 0:
                break
            case _:
                print("Opção digitada inválida tente novamente!")

        session.close()
if __name__ == "__main__":
    os.system("cls || clear")
    main()