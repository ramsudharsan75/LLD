from dataclasses import dataclass
from random import randint

from src.tic_tac_toe.domain.value_object.symbol import Symbol

from src.tic_tac_toe.domain.entity.player import Player
from src.tic_tac_toe.domain.entity.board import Board
from src.shared.domain.entity import AggregateRoot


@dataclass(eq=False)
class Game(AggregateRoot):
    board: Board
    players: list[Player]
    current_player: Player
    winner: Player | None = None
    has_ended: bool = False

    def __init__(self) -> None:
        self.board = Board()
        self.players = [
            Player(Symbol.X),
            Player(Symbol.O),
        ]
        self.current_player = self.players[randint(0, 1)]

    def mark(self, row: int, col: int):
        if self.has_ended:
            raise ValueError("Game is over")

        self.board.fill(row, col, self.current_player.symbol)

        if self._has_winner():
            self.winner = self.current_player

        if self.board.is_full() or self.winner:
            self.has_ended = True
        else:
            self._switch_next_turn()

    def _has_winner(self):
        return self._check_rows() or self._check_cols() or self._check_diagonals()

    def _check_rows(self):
        for row in self.board.grid:
            if row[0] == row[1] == row[2] != Symbol.EMPTY:
                return True

        return False

    def _check_cols(self):
        for col in range(3):
            if (
                self.board.grid[0][col]
                == self.board.grid[1][col]
                == self.board.grid[2][col]
                != Symbol.EMPTY
            ):
                return True

        return False

    def _check_diagonals(self):
        if (
            self.board.grid[0][0]
            == self.board.grid[1][1]
            == self.board.grid[2][2]
            != Symbol.EMPTY
        ):
            return True

        if (
            self.board.grid[0][2]
            == self.board.grid[1][1]
            == self.board.grid[2][0]
            != Symbol.EMPTY
        ):
            return True

        return False

    def _switch_next_turn(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
