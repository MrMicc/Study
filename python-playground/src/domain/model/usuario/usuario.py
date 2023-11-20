
from src.domain.model.exception.customException import NomeInvalidoError


class Usuario():

    def __init__(self, nome) -> None:
        if not nome:
            raise NomeInvalidoError("Nome Invalido!")
        #verify if nome is a string
        if not isinstance(nome, str):
            raise NomeInvalidoError("Nome Invalido!")
        #nome cannot have numbers
        if any(char.isdigit() for char in nome):
            raise NomeInvalidoError("Nome Invalido!")

        #nome cannot start with space and end with space
        if nome[0].isspace() or nome[-1].isspace():
            raise NomeInvalidoError("Nome Invalido!")

        self.nome = nome
