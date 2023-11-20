
from src.domain.model.exception.customException import NomeInvalidoError


class Usuario():

    def __init__(self, nome) -> None:
        if not nome:
            raise NomeInvalidoError("Nome Invalido!")
        #verify if nome is a string
        if not isinstance(nome, str):
            raise NomeInvalidoError("Nome Invalido! Não pode conter números!")
        #nome cannot have numbers
        if any(char.isdigit() for char in nome):
            raise NomeInvalidoError("Nome Invalido! Não pode conter números!")

        self.nome = " ".join(nome.split())
