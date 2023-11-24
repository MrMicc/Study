
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
        character_especiais = "@#$%^&*()-+?_=,<>!/."
        if not email:
            raise EmailInvalidoError("Email Invalido!")
        #check se o email começa ou termina com carcter especiais
        if email[0] in character_especiais or email[-1] in character_especiais:
            raise EmailInvalidoError("Email Invalido! Email pode comecar ou terminar com caracteres especiais!")
        #check se o email possui @
        if "@" not in email:
            raise EmailInvalidoError("Email Invalido! Email deve conter @!")
        #check se email possuim mais de um @
        if email.count("@") > 1:
            raise EmailInvalidoError("Email Invalido! Email nao pode conter mais de um @!")\
        #check se o email tem um ponto apos o arroba
        if "." not in email.split("@")[1]:
            raise EmailInvalidoError("Email Invalido! Email deve conter ponto apos o @!")

        #check se email possui mais de 3 caracteres antes do arroba
        if len(email.split("@")[0]) < 3:
            raise EmailInvalidoError("Email Invalido! Email deve conter mais de 2 caracteres antes do @!")

        #check se email possui mais de 3 caracteres depois do arroba
        if len(email.split("@")[1]) < 3:
            raise EmailInvalidoError("Email Invalido! Email deve conter mais de 2 caracteres depois do @!")
        return True

    @property
    def nome(self):
        """The nome property."""
        return self.__nome

    @property
    def email(self) -> str:
        """Email property."""
        return self.__email
