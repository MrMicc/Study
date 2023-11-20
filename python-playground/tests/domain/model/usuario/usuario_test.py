from src.domain.model import usuario
from src.domain.model.usuario.usuario import Usuario
from src.domain.model.exception.customException import NomeInvalidoError
import pytest


class TestUsuario():

    @pytest.mark.parametrize("nome", ["Micci", "Luiz",
                                      "João", " Luis", " Marcia ", "vica ", "luiz    felipe", "Luiz Felipe"])
    def test_criando_usuario_dados_minimos(self, nome):
        usuario = Usuario(nome)
        assert usuario.nome ==" ".join(nome.split())

    @pytest.mark.parametrize("nome", ["", None])
    def test_nome_nao_pode_ter_vazio(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
              Usuario(nome)
        assert str(target.value) == "Nome Invalido!"


    @pytest.mark.parametrize("nome", [123, 123.0, '123', 'Micci123'])
    def test_nome_nao_pode_ser_numerico(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            Usuario(nome)
        assert str(target.value) == "Nome Invalido! Não pode conter números!"
   

    @pytest.mark.parametrize("nome", ["n@me", "Lu!z", "Jo@o", "Luis&", "$hirley", "marc*s"])
    def test_nome_nao_pode_conter_caracteres_especiais(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            Usuario(nome)
        assert str(target.value) == "Nome Invalido! Nome pode conter caracteres especiais!"
