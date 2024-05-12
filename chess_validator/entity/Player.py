from LLD.chess_validator.util.enum import PieceColourEnum


class Player:
    def __init__(self, piece_colour: PieceColourEnum) -> None:
        self.piece_colour = piece_colour
