from LLD.chess_validator.strategy.MoveStrategy import MoveStrategy
from LLD.chess_validator.util.enum import PieceColourEnum, PieceTypeEnum


class Piece:
    def __init__(
        self,
        piece_name: str,
        piece_colour: PieceColourEnum,
        piece_type: PieceTypeEnum,
        move_strategy: type[MoveStrategy],
    ) -> None:
        self.piece_name = piece_name
        self.piece_colour = piece_colour
        self.piece_type = piece_type
        self.move_strategy = move_strategy
