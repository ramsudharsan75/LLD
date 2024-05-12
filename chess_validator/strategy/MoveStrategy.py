from abc import ABC, abstractmethod

from LLD.chess_validator.entity.Board import Board
from LLD.chess_validator.entity.Piece import Piece
from LLD.chess_validator.util.enum import PieceColourEnum


class MoveStrategy(ABC):
    @staticmethod
    @abstractmethod
    def is_piece_move_valid(
        board: Board, curr_piece: Piece, from_pos: str, to_pos: str
    ) -> bool:
        pass


class PawnMoveStrategy(MoveStrategy):
    @staticmethod
    def is_piece_move_valid(
        board: Board, curr_piece: Piece, from_pos: str, to_pos: str
    ) -> bool:
        row_direction = 1 if curr_piece.piece_colour == PieceColourEnum.WHITE else -1
        initial_row = 1 if curr_piece.piece_colour == PieceColourEnum.WHITE else 7
        from_col, from_row = ord(from_pos[0]) - 96, int(from_pos[1])
        to_col, to_row = ord(to_pos[0]) - 96, int(to_pos[1])
        pieces = board.pieces

        if to_row == from_row + row_direction:
            return to_col == from_col or (
                to_col == from_col - 1
                or to_col == from_col + 1
                and chr(to_col + 96) + str(to_row) in pieces
            )

        if from_row == initial_row and to_row == from_row + 2 * row_direction:
            return (
                to_col == from_col
                and chr(to_col + 96) + str(to_row) not in pieces
                and chr(to_col + 96) + str(to_row - row_direction) not in pieces
            )

        return False


class RookMoveStrategy(MoveStrategy):
    @staticmethod
    def is_piece_move_valid(
        board: Board, curr_piece: Piece, from_pos: str, to_pos: str
    ) -> bool:
        from_col, from_row = ord(from_pos[0]) - 96, int(from_pos[1])
        to_col, to_row = ord(to_pos[0]) - 96, int(to_pos[1])
        pieces = board.pieces

        if from_row != to_row and from_col == to_col:
            start_row, end_row = from_row, to_row

            if end_row < start_row:
                start_row, end_row = end_row, start_row

            return not any(
                chr(to_col + 96) + str(row) in pieces
                for row in range(start_row + 1, end_row)
            )
        elif from_col != to_col and from_row == to_row:
            start_col, end_col = from_col, to_col

            if end_col < start_col:
                start_col, end_col = end_col, start_col

            return not any(
                chr(to_col + 96) + str(row) in pieces
                for row in range(start_col + 1, end_col)
            )

        return False


class KnightMoveStrategy(MoveStrategy):
    pass


class BishopMoveStrategy(MoveStrategy):
    pass


class QueenMoveStrategy(MoveStrategy):
    pass


class KingMoveStrategy(MoveStrategy):
    pass
