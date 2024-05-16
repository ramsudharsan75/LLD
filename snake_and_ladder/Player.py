import random
from typing import Self

from .Die import Die


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.position = 0

    def roll_die(self, die: Die) -> int:
        face = random.randint(1, die.faces)
        return face

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Self) -> bool:
        return self.name == other.name

    def __str__(self) -> str:
        return self.name
