from typing import TYPE_CHECKING

from LLD.chess_validator.entity.Piece import Piece
from LLD.chess_validator.strategy.MoveStrategy import (
    BishopMoveStrategy,
    KingMoveStrategy,
    KnightMoveStrategy,
    PawnMoveStrategy,
    QueenMoveStrategy,
    RookMoveStrategy,
)
from LLD.chess_validator.util.enum import PieceColourEnum, PieceTypeEnum

if TYPE_CHECKING:
    from LLD.chess_validator.entity.Board import Board


class PieceFactory:
    @staticmethod
    def create_army(piece_colour: PieceColourEnum):
        prefix = "W" if piece_colour == PieceColourEnum.WHITE else "B"
        pawns = [
            Piece(
                piece_name=prefix + "P",
                piece_colour=piece_colour,
                piece_type=PieceTypeEnum.PAWN,
                move_strategy=PawnMoveStrategy,
            )
            for _ in range(8)
        ]
        rooks = [
            Piece(
                piece_name=prefix + "R",
                piece_colour=piece_colour,
                piece_type=PieceTypeEnum.ROOK,
                move_strategy=RookMoveStrategy,
            )
            for _ in range(2)
        ]
        knights = [
            Piece(
                piece_name=prefix + "K",
                piece_colour=piece_colour,
                piece_type=PieceTypeEnum.KNIGHT,
                move_strategy=KnightMoveStrategy,
            )
            for _ in range(2)
        ]
        bishops = [
            Piece(
                piece_name=prefix + "B",
                piece_colour=piece_colour,
                piece_type=PieceTypeEnum.BISHOP,
                move_strategy=BishopMoveStrategy,
            )
            for _ in range(2)
        ]
        queen = [
            Piece(
                piece_name=prefix + "Q",
                piece_colour=piece_colour,
                piece_type=PieceTypeEnum.QUEEN,
                move_strategy=QueenMoveStrategy,
            )
        ]
        king = [
            Piece(
                piece_name=prefix + "K",
                piece_colour=piece_colour,
                piece_type=PieceTypeEnum.KING,
                move_strategy=KingMoveStrategy,
            )
        ]

        return {
            PieceTypeEnum.PAWN: pawns,
            PieceTypeEnum.ROOK: rooks,
            PieceTypeEnum.KNIGHT: knights,
            PieceTypeEnum.BISHOP: bishops,
            PieceTypeEnum.QUEEN: queen,
            PieceTypeEnum.KING: king,
        }
