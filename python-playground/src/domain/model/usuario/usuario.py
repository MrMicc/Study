from src.domain.model.exception.customException import *
from enum import Enum


class UsuarioValidacoes(Enum):
    NOME_INVALIDO = "Nome Invalido!"
    NOME_NAO_PODE_TER_NUMEROS = "Nome Invalido! Não pode conter números!"
    NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS = "Nome Invalido! Nome pode conter caracteres especiais!"
    NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR = "Nome Invalido! Nome deve ter pelo menos 3 caracteres"
    NOME_PRECISA_SER_STRING = "Nome invalido! Nome precisa ser do tipo String"

    EMAIL_NAO_PODE_COMECAR_OU_TERMINAR_COM_CARACTERES_ESPECIAIS = "Email Invalido! Email nao pode comecar ou terminar com caracteres especiais!"
    EMAIL_DEVE_CONTER_ARROBA = "Email Invalido! Email deve conter @"
    EMAIL_NAO_PODE_CONTER_MAIS_QUE_UM_ARROBA = "Email Invalido! Email nao pode conter mais de um @!"
    EMAIL_DEVE_CONTER_PONTOS_APOS_ARROBA = "Email Invalido! Email deve conter ponto apos o @!"
    EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_ANTES_ARROBA = "Email Invalido! Email deve conter mais de 2 caracteres antes do @!"
    EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_DEPOIS_ARROBA = "Email Invalido! Email deve conter mais de 2 caracteres depois do @!"

    CARACTERES_ESPECIAIS = "@#$%^&*()-+?_=,<>!/."


class Usuario():

    __caracter_especiais = UsuarioValidacoes.CARACTERES_ESPECIAIS.value

    def __init__(self, nome: str, email: str) -> None:

        if self.__checa_se_nome_valido(nome):
            self.__nome = " ".join(nome.split())

        if self.__checa_se_email_valido(email):
            self.__email = "".join(email.split())

    def __checa_se_nome_valido(self, nome: str) -> bool:
        lista_erros = []
        if not nome:
            lista_erros.append(UsuarioValidacoes.NOME_INVALIDO.value)
        # verify if nome is a string
        if not isinstance(nome, str):
            lista_erros.append(UsuarioValidacoes.NOME_PRECISA_SER_STRING.value)
            raise NomeInvalidoError(lista_erros)

        if isinstance(nome, str) and any(char.isdigit() for char in nome):
            lista_erros.append(
                UsuarioValidacoes.NOME_NAO_PODE_TER_NUMEROS.value)
        # nome cannot have special characters
        if any(char in self.__caracter_especiais for char in nome):
            lista_erros.append(
                UsuarioValidacoes.NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS.value)
        # nome needs to be at least 3 characters long
        if len(nome) < 3:
            lista_erros.append(
                UsuarioValidacoes.NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR.value)

        if len(lista_erros) > 0:
            print(lista_erros)
            raise NomeInvalidoError(lista_erros)
        return True

    def __checa_se_email_valido(self, email: str) -> bool:
        lista_erros = []
        character_especiais = self.__caracter_especiais
        if not email:
            raise EmailInvalidoError("Email Invalido!")
        # check se o email começa ou termina com carcter especiais
        if email[0] in character_especiais or email[-1] in character_especiais:
            lista_erros.append(
                UsuarioValidacoes.EMAIL_NAO_PODE_COMECAR_OU_TERMINAR_COM_CARACTERES_ESPECIAIS.value)
        # check se o email possui @
        if "@" not in email:
            lista_erros.append(
                UsuarioValidacoes.EMAIL_DEVE_CONTER_ARROBA.value)
        # check se email possuim mais de um @
        else:
            if email.count("@") > 1:
                lista_erros.append(
                    UsuarioValidacoes.EMAIL_NAO_PODE_CONTER_MAIS_QUE_UM_ARROBA.value)
            # check se o email tem um ponto apos o arroba
            if "." not in email.split("@")[1]:
                lista_erros.append(
                    UsuarioValidacoes.EMAIL_DEVE_CONTER_PONTOS_APOS_ARROBA.value)
             # check se email possui mais de 3 caracteres antes do arroba
            if len(email.split("@")[0]) < 3:
                lista_erros.append(
                    UsuarioValidacoes.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_ANTES_ARROBA.value)
            # check se email possui mais de 3 caracteres depois do arroba
            if len(email.split("@")[1]) < 3:
                lista_erros.append(
                    UsuarioValidacoes.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_DEPOIS_ARROBA.value)

        if len(lista_erros) > 0:
            raise EmailInvalidoError(lista_erros)
        return True

    @property
    def caracteres_especiais(self) -> str:
        """This caracters_especiais property."""
        return self.__caracter_especiais

    @property
    def nome(self):
        """The nome property."""
        return self.__nome

    @property
    def email(self) -> str:
        """Email property."""
        return self.__email
