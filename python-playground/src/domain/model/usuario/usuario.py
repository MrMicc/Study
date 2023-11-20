
from src.domain.model.exception.customException import NomeInvalidoError


class Usuario():

    def __init__(self, nome) -> None:
        if not nome:
            raise NomeInvalidoError("Nome Invalido!")
        self.nome = nome
