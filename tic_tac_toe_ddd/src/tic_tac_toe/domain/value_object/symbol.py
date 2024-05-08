from enum import Enum
from src.shared.domain.value_object import ValueObject


class Symbol(ValueObject, Enum):
    X = "X"
    O = "O"
    EMPTY = "EMPTY"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()
