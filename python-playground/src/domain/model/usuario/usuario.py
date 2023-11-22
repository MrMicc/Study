
from src.domain.model.exception.customException import NomeInvalidoError


class Usuario():

    caracter_especiais = "@#$%^&*()-+?_=,<>!/"

    def __init__(self, nome:str, email:str) -> None:
        if self.__checa_se_nome_valido(nome):
            self.__nome = " ".join(nome.split())

        self.__email = email
    


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

    @property
    def nome(self):
        """The nome property."""
        return self.__nome

    @property
    def email(self) -> str:
        """doc"""
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
