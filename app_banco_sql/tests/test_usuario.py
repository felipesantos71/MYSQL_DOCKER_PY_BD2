import pytest

from app_banco_sql.models.usuario_model import Usuario

@pytest.fixture

def usuario_valido():
    return Usuario("Diana", "dianasilva@gmail.com", "456")

def test_nome_vazio():
    with pytest.raises(ValueError, match="Não é permitido informação nula."):
        Usuario("", "dianasilva@gmail.com", "456")

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="Tipo do valor inválido."):
        Usuario(112, "dianasilva@gmail.com", "456")

def test_email_vazio():
    with pytest.raises(ValueError, match="Não é permitido informação nula."):
        Usuario("Diana", "", "456")

def test_email_tipo_invalido():
    with pytest.raises(TypeError, match="Tipo do valor inválido."):
        Usuario("Diana", 654, "456")

def test_senha_vazio():
    with pytest.raises(ValueError, match="Não é permitido informação nula."):
        Usuario("Diana", "dianasilva@gmail.com", "")

def test_senha_tipo_invalido():
    with pytest.raises(TypeError, match="Tipo do valor inválido."):
        Usuario("Diana", "dianasilva@gmail.com", 456)