from LLD.chess_validator.entity.Piece import Piece
from LLD.chess_validator.entity.Player import Player
from LLD.chess_validator.factory.PieceFactory import PieceFactory
from LLD.chess_validator.util.enum import PieceColourEnum, PieceTypeEnum


class Board:
    def __init__(
        self, colours: list[PieceColourEnum], rows: int = 8, cols: int = 8
    ) -> None:
        self.rows = rows
        self.cols = cols
        self.colours = colours

        self.pieces: dict[str, Piece] = {}
        self.cut_pieces: set[Piece] = set()
        self.populate_pieces()

    def populate_pieces(self):
        for colour in self.colours:
            army: dict[PieceTypeEnum, list[Piece]] = PieceFactory.create_army(colour)
            self._position_army(colour, army)

    def _position_army(
        self, piece_colour: PieceColourEnum, army: dict[PieceTypeEnum, list[Piece]]
    ):
        pawn_row = "2" if piece_colour == PieceColourEnum.WHITE else "7"
        other_piece_row = "1" if piece_colour == PieceColourEnum.WHITE else "8"

        self.pieces = {
            "a" + pawn_row: army[PieceTypeEnum.PAWN][0],
            "b" + pawn_row: army[PieceTypeEnum.PAWN][1],
            "c" + pawn_row: army[PieceTypeEnum.PAWN][2],
            "d" + pawn_row: army[PieceTypeEnum.PAWN][3],
            "e" + pawn_row: army[PieceTypeEnum.PAWN][4],
            "f" + pawn_row: army[PieceTypeEnum.PAWN][5],
            "g" + pawn_row: army[PieceTypeEnum.PAWN][6],
            "h" + pawn_row: army[PieceTypeEnum.PAWN][7],
            "a" + other_piece_row: army[PieceTypeEnum.ROOK][0],
            "h" + other_piece_row: army[PieceTypeEnum.ROOK][1],
            "b" + other_piece_row: army[PieceTypeEnum.KNIGHT][0],
            "g" + other_piece_row: army[PieceTypeEnum.KNIGHT][1],
            "c" + other_piece_row: army[PieceTypeEnum.BISHOP][0],
            "f" + other_piece_row: army[PieceTypeEnum.BISHOP][1],
            "d" + other_piece_row: army[PieceTypeEnum.QUEEN][0],
            "e" + other_piece_row: army[PieceTypeEnum.KING][0],
        }

    def is_move_valid(self, curr_player: Player, from_pos: str, to_pos: str):
        if (
            not self.is_move_within_limits(to_pos)
            or not self._is_there_a_piece(from_pos)
            or not self._are_players_matching(curr_player, from_pos)
        ):
            return False

        piece = self.pieces[from_pos]

        if self._does_overlap_with_same_coloured_piece(
            piece, to_pos
        ) or not piece.move_strategy.is_piece_move_valid(self, piece, from_pos, to_pos):
            return False

        return True

    def is_move_within_limits(self, to_pos: str):
        col, row = to_pos[0], int(to_pos[1])
        return (
            True if 1 <= row <= self.rows and 1 <= ord(col) - 96 <= self.cols else False
        )

    def _is_there_a_piece(self, from_pos: str):
        return from_pos in self.pieces

    def _are_players_matching(self, curr_player: Player, from_pos: str):
        piece = self.pieces[from_pos]
        return piece.piece_colour == curr_player.piece_colour

    def _does_overlap_with_same_coloured_piece(self, curr_piece: Piece, to_pos: str):
        if to_pos in self.pieces:
            other_piece = self.pieces[to_pos]
            return other_piece.piece_colour == curr_piece.piece_colour

        return False

    def update_pos(self, from_pos: str, to_pos: str):
        if to_pos in self.pieces:
            self.cut_pieces.add(self.pieces[to_pos])

        piece = self.pieces[from_pos]
        del self.pieces[from_pos]
        self.pieces[to_pos] = piece
