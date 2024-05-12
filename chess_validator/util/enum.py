from enum import Enum


class PieceColourEnum(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"


class PieceTypeEnum(Enum):
    PAWN = "PAWN"
    ROOK = "ROOK"
    KNIGHT = "KNIGHT"
    BISHOP = "BISHOP"
    QUEEN = "QUEEN"
    KING = "KING"
