from src.domain.model.usuario.usuario import Usuario, UsuarioValidacoes
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
        assert str(target.value) == UsuarioValidacoes.NOME_INVALIDO.value 

    @pytest.mark.parametrize("nome", [123, 123.0, '123', 'Micci123'])
    def test_nome_nao_pode_ser_numerico(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert str(target.value) == UsuarioValidacoes.NOME_NAO_PODE_TER_NUMEROS.value

    @pytest.mark.parametrize("nome", ["n@me", "Lu!z", "Jo@o", "Luis&", "$hirley", "marc*s"])
    def test_nome_nao_pode_conter_caracteres_especiais(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert str(
            target.value) == UsuarioValidacoes.NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS.value

    @pytest.mark.parametrize("nome", ["An", "a", "zu"])
    def test_nome_nao_pode_conter_menos_de_3_caracteres(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert str(
            target.value) == UsuarioValidacoes.NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR.value

    """
    ###################### VALIDAÇÕES DO ATRIBUTO EMAIL ####################
    """
    # validações do atributo email\
    @pytest.mark.parametrize("email", ["", None])
    def test_email_nao_pode_ser_vazio(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido!"

    @pytest.mark.parametrize("email", ["emai @email.com", "e mail@ mail.com"])
    def test_email_remover_espacos(self,email: str):
        usuario = self.criar_usuario(email=email)
        assert usuario.email == "".join(email.split())

    #email não pode comecar ou terminar com caracteres especiais
    @pytest.mark.parametrize("email", ["@email.com", ".email@.com", "!email@.com", ".email.com.",
    "email@.com."])
    def test_email_nao_pode_comecar_ou_terminar_com_caracteres_especiais(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            usuario = self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido! Email pode comecar ou terminar com caracteres especiais!"

    """
    quadno email não tiver pelo menos um @
    entao um erro deve ser gerado E informar que email é invalido
    """
    @pytest.mark.parametrize("email", ["email.mail", "email"])
    def test_email_deve_conter_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido! Email deve conter @!"


    """
    quando email tiver mais de um @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["email@email@.com", "email@email@.com", "email@@mail"])
    def test_email_nao_pode_conter_mais_de_um_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido! Email nao pode conter mais de um @!"

    """
    quuando o não existir um ponto apos o @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["email@mail", "meu.email@mail"])
    def test_email_deve_conter_ponto_apos_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido! Email deve conter ponto apos o @!"

    """
    quando email não tiver ao menos 3 caracteres antes do @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["an@email.com", "a@mail.com.net"])
    def test_email_deve_conter_3_caracteres_antes_do_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido! Email deve conter mais de 2 caracteres antes do @!"

    """
    quando email não tiver ao menos 3 caracteres depois do @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["emai@.a"])
    def test_email_deve_conter_3_caracteres_depois_do_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido! Email deve conter mais de 2 caracteres depois do @!"

    """
    quando email estiver valido 
    então atributo email deve ser igual a email
    """
    @pytest.mark.parametrize("email", ["email@.com", "email@.com.br", "meu+email@mail.com.br", "meu-email@mail.com", "em123@mail.com.net"])
    def test_email_deve_ser_igual_a_email(self, email:str):
        usuario = self.criar_usuario(email=email)
        assert usuario.email == email




