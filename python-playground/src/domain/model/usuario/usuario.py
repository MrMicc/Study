
from src.domain.model.exception.customException import *


class Usuario():

    caracter_especiais = "@#$%^&*()-+?_=,<>!/"

    def __init__(self, nome: str, email: str) -> None:
        if self.__checa_se_nome_valido(nome):
            self.__nome = " ".join(nome.split())

        if self.__checa_se_email_valido(email):
            self.__email = "".join(email.split())

    def __checa_se_nome_valido(self, nome: str) -> bool:
        if not nome:
            raise NomeInvalidoError("Nome Invalido!")
        # verify if nome is a string
        if not isinstance(nome, str):
            raise NomeInvalidoError("Nome Invalido! Não pode conter números!")
        # nome cannot have numbers
        if any(char.isdigit() for char in nome):
            raise NomeInvalidoError("Nome Invalido! Não pode conter números!")
        # nome cannot have special characters
        if any(char in self.caracter_especiais for char in nome):
            raise NomeInvalidoError(
                "Nome Invalido! Nome pode conter caracteres especiais!")
        # nome needs to be at least 3 characters long
        if len(nome) < 3:
            raise NomeInvalidoError(
                "Nome Invalido! Nome deve ter mais de 3 caracteres!")
        return True

    def __checa_se_email_valido(self, email: str) -> bool:
        if not email:
            raise EmailInvalidoError("Email Invalido!")
        return True

    @property
    def nome(self):
        """The nome property."""
        return self.__nome

    @property
    def email(self) -> str:
        """Email property."""
        return self.__email
