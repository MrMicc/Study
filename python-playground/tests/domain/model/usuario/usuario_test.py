from src.domain.model import usuario
from src.domain.model.usuario.usuario import Usuario
from src.domain.model.exception.customException import *
import pytest


class TestUsuario():

    def criar_usuario(self, nome: str = "Teste", email: str = "email@email.com"):
        return Usuario(nome, email)

    @pytest.mark.parametrize("nome", ["Micci", "Luiz", "udy"
                                      "João", " Luis", " Marcia ", "vica ", "luiz    felipe", "Luiz Felipe"])
    def test_criando_usuario_dados_minimos(self, nome):
        usuario = self.criar_usuario(nome)
        assert usuario.nome == " ".join(nome.split())

    @pytest.mark.parametrize("nome", ["", None])
    def test_nome_nao_pode_ter_vazio(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert str(target.value) == "Nome Invalido!"

    @pytest.mark.parametrize("nome", [123, 123.0, '123', 'Micci123'])
    def test_nome_nao_pode_ser_numerico(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert str(target.value) == "Nome Invalido! Não pode conter números!"

    @pytest.mark.parametrize("nome", ["n@me", "Lu!z", "Jo@o", "Luis&", "$hirley", "marc*s"])
    def test_nome_nao_pode_conter_caracteres_especiais(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert str(
            target.value) == "Nome Invalido! Nome pode conter caracteres especiais!"

    @pytest.mark.parametrize("nome", ["An", "a", "zu"])
    def test_nome_nao_pode_conter_menos_de_3_caracteres(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert str(
            target.value) == "Nome Invalido! Nome deve ter mais de 3 caracteres!"

    # validações do atributo email
    @pytest.mark.parametrize("email", ["", None])
    def test_email_nao_pode_ser_vazio(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido!"
