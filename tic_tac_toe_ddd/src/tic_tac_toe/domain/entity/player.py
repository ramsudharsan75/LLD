from dataclasses import dataclass


from src.tic_tac_toe.domain.value_object.symbol import Symbol
from src.shared.domain.entity import Entity


@dataclass(eq=False)
class Player(Entity):
    symbol: Symbol

    def play(self, game):
        row, col = self._collect_row_col()

        try:
            game.mark(row, col)
        except ValueError as e:
            print(e)
            self.play(game)

    def _collect_row_col(self):
        print(f"Player {self.symbol.value} turn")
        row: int = int(input("Enter row: "))
        col: int = int(input("Enter col: "))

        return row, col
