from dataclasses import dataclass, field
from src.shared.domain.entity import Entity
from src.tic_tac_toe.domain.value_object.symbol import Symbol


@dataclass(eq=False)
class Board(Entity):
    grid: list[list[Symbol]] = field(
        default_factory=lambda: [[Symbol.EMPTY for _ in range(3)] for _ in range(3)]
    )

    def fill(self, row: int, col: int, symbol: Symbol):
        if self.grid[row][col] != Symbol.EMPTY:
            raise ValueError("Position already taken")

        self.grid[row][col] = symbol

    def is_full(self):
        for row in self.grid:
            for col in row:
                if col == Symbol.EMPTY:
                    return False

        return True
