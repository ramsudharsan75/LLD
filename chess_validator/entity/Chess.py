from collections import deque

from LLD.chess_validator.entity.Board import Board
from LLD.chess_validator.entity.Player import Player
from LLD.chess_validator.service.InputReaderService import InputReaderService
from LLD.chess_validator.util.enum import PieceColourEnum


class Chess:
    def __init__(self) -> None:
        colours = [PieceColourEnum.WHITE, PieceColourEnum.BLACK]
        self.players = deque(Player(colour) for colour in colours)
        self.board = Board(colours)
