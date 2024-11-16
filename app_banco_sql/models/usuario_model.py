from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app_banco_sql.config.database import db

Base = declarative_base()

class Usuario(Base):
    #Definindo caracteristicas da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    #Definindo caracteristicas da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificando_valor_tipo(nome)
        self.email = self._verificando_valor_tipo(email)
        self.senha = self._verificando_valor_tipo(senha)

    def _verificar_valor_tipo(valor, self):
        if not isinstance(valor, str):
            raise TypeError("Tipo do valor inválido.")
        if not valor.strip():
            raise ValueError("Não é permitido informação nula.")
        return valor
    
#Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)