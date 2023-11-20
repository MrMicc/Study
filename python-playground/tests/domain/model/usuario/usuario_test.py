from src.domain.model import usuario
from src.domain.model.usuario.usuario import Usuario
from src.domain.model.exception.customException import NomeInvalidoError
import pytest


class TestUsuario():

    def test_criando_usuario_dados_minimos(self):
        usuario = Usuario("nome")
        assert usuario.nome == "nome"

    def test_nome_nao_pode_ter_vazio(self):
        with pytest.raises(NomeInvalidoError) as target:
              Usuario("")
        assert str(target.value) == "Nome Invalido!"

        with pytest.raises(NomeInvalidoError) as target:
            Usuario(None)
        assert str(target.value) == "Nome Invalido!"

    def test_nome_nao_pode_ser_numerico(self):
        with pytest.raises(NomeInvalidoError) as target:
            Usuario('123')
        assert str(target.value) == "Nome Invalido!"
       
        with pytest.raises(NomeInvalidoError) as target:
            Usuario(123)
        assert str(target.value) == "Nome Invalido!"
