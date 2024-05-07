from collections import deque
from sqlite3 import DataError

from LLD.snake_and_ladder.Board import Board, Ladder, Snake
from LLD.snake_and_ladder.Die import Die
from LLD.snake_and_ladder.Player import Player


class Game:
    def __init__(self, board: Board, players: set[Player], die: Die) -> None:
        self.board = board
        self.players = players
        self.die = die

        self.player_turns: deque[Player]
        self.has_winner = False

    @staticmethod
    def start():
        snakes: set[Snake] = set()
        ladders: set[Ladder] = set()
        players: set[Player] = set()
        board = Board(snakes, ladders)
        die = Die(faces=6)
        game = Game(board, players, die)
        game.populate_snakes(board)
        game.populate_ladders(board)
        game.populate_players(game)
        game.populate_player_list()

        while not game.has_winner:
            game.play()

    @staticmethod
    def populate_snakes(board: Board):
        no_of_snakes = int(input("Enter number of snakes:").strip())

        for i in range(no_of_snakes):
            pos = input(f"Enter position for snake {i + 1}: ").strip().split(" ")
            head, tail = int(pos[0]), int(pos[1])
            board.add_snake(Snake(head, tail))

    @staticmethod
    def populate_ladders(board: Board):
        no_of_ladders = int(input("Enter number of ladders").strip())

        for i in range(no_of_ladders):
            pos = input(f"Enter position for ladder {i + 1}: ").strip().split(" ")
            start, end = int(pos[0]), int(pos[1])
            board.add_ladder(Ladder(start, end))

    @staticmethod
    def populate_players(game: "Game"):
        no_of_players = int(input("Enter number of players").strip())

        for i in range(no_of_players):
            game.add_player(Player(input(f"Enter player {i + 1} name: ").strip()))

    def add_player(self, player: Player):
        if player in self.players:
            raise ValueError("Player already exists")

        self.players.add(player)

    def populate_player_list(self):
        self.player_turns = deque(self.players)

    def play(self):
        board = self.board

        next_player = self._get_next_player()
        face = next_player.roll_die(self.die)
        board.update_player_position(next_player, face)

        if next_player.position == 100:
            self.has_winner = True
            print(f"{next_player} wins the game")

    def _get_next_player(self) -> Player:
        if not self.player_turns:
            raise DataError("No player found")

        next_player = self.player_turns.popleft()
        self.player_turns.append(next_player)
        return next_player
