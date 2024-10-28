from services.usuario_services import UsuarioService
from repositores.usuario_repositore import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Solicitando dados para o usuario
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite seu senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)


    #Listar todos os usuarios cadastrados
    print("\nListando usuarios cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")
    main() 